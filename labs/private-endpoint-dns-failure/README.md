# Lab substrate: Private-endpoint DNS failure

This substrate deploys the minimum Azure resources needed to reproduce a storage private-endpoint DNS path failure: a blob storage account, a blob private endpoint, the `privatelink.blob.core.windows.net` private DNS zone, a VNet link, and a client VM that can run `nslookup` from the private network path.

The healthy baseline is: `nslookup <storage-account>.blob.core.windows.net` from the client VM resolves to the private endpoint IP. The fault injection for this substrate removes the private DNS VNet link so the same lookup falls back to a public or otherwise wrong answer.

## Purpose

- Provide a valid offline-authored substrate for issue #22 (`ZLR-storage-02`).
- Keep the fault model narrow: DNS path breakage, not storage account creation failure.
- Reserve live deployment, live evidence capture, and final lab-guide authoring for later work.

## Structure

```text
labs/private-endpoint-dns-failure/
├── main.bicep
├── parameters.dev.json
├── README.md
├── evidence/
│   └── README.md
└── scripts/
    ├── cleanup.sh
    └── reproduce.sh
```

## Prerequisites

- Azure CLI with Bicep support.
- Permission to create a resource group, storage account, private endpoint, private DNS zone, private DNS VNet link, and VM.
- A real SSH public key substituted into `parameters.dev.json` or supplied at deployment time.
- A test resource group name in `$RG`.

## Deploy the substrate

Set environment variables and run the lab script. The script creates the resource group, deploys `main.bicep`, and by default injects the DNS fault immediately after the deployment succeeds.

```bash
export RG="rg-storage-pe-dns-lab"
export LOCATION="koreacentral"
export INJECT_FAULT="true"

bash labs/private-endpoint-dns-failure/scripts/reproduce.sh
```

If you want to inspect the healthy state before deleting the VNet link, run the same script with `INJECT_FAULT="false"`, validate the private answer, and then delete the VNet link manually with the command in the next section.

## Fault injection step

The substrate uses a single documented DNS fault: delete the VNet link that lets the client VNet resolve `privatelink.blob.core.windows.net`.

```bash
export ZONE_LINK_NAME="blob-zone-link"

az network private-dns link vnet delete \
    --resource-group "$RG" \
    --zone-name privatelink.blob.core.windows.net \
    --name "$ZONE_LINK_NAME" \
    --yes
```

| Command | Purpose |
| --- | --- |
| `az network private-dns link vnet delete` | Remove the client VNet link from the blob private DNS zone to trigger the DNS-resolution failure. |
| `--resource-group` | Scope the delete operation to the lab resource group. |
| `--zone-name` | Select the blob private DNS zone used by the storage private endpoint. |
| `--name` | Select the VNet link resource that the lab deployed. |
| `--yes` | Skip the interactive confirmation prompt for scripted fault injection. |


## Expected symptom

Run `nslookup` from the client VM by using Azure Run Command. After the VNet link is deleted, the storage account FQDN should no longer resolve to the private endpoint IP on the private path.

```bash
export VM_NAME="pednslab-vm"
export STORAGE_NAME="stpednslab001"

az vm run-command invoke \
    --resource-group "$RG" \
    --name "$VM_NAME" \
    --command-id RunShellScript \
    --scripts "nslookup ${STORAGE_NAME}.blob.core.windows.net"
```

| Command | Purpose |
| --- | --- |
| `az vm run-command invoke` | Execute `nslookup` inside the client VM without requiring inbound SSH access. |
| `--resource-group` | Scope the VM lookup to the lab resource group. |
| `--name` | Identify the client VM that sits on the private access path. |
| `--command-id` | Use the built-in shell runner for Linux VMs. |
| `--scripts` | Run `nslookup` against the storage account blob endpoint from inside the client network. |


Expected lab symptom for later live validation:

- Healthy state: `${STORAGE_NAME}.blob.core.windows.net` resolves to the private endpoint IP.
- Faulted state: `${STORAGE_NAME}.blob.core.windows.net` resolves to a public IP, public CNAME chain, or another non-private answer because the private DNS zone is no longer linked to the client VNet.

## Evidence artifacts

Real artifacts are intentionally deferred until a live Azure run. During the future live run, capture at least:

- `az deployment group show` output for the lab deployment.
- `az network private-endpoint show` output proving the private endpoint private IP.
- `az network private-dns link vnet list` output before and after the fault injection.
- `nslookup <storage-account>.blob.core.windows.net` output from the client VM before and after the fault injection.
- Any recovery step output if the VNet link is recreated.

Do not add fake JSON, screenshots, or command output to `evidence/` before a real deployment happens.

## Cleanup

```bash
export RG="rg-storage-pe-dns-lab"
bash labs/private-endpoint-dns-failure/scripts/cleanup.sh
```

## See Also

- `docs/troubleshooting/playbooks/access/private-endpoint-and-dns-issues.md`
- `docs/operations/use-private-endpoints.md`
- `docs/tutorials/lab-guides/lab-02-private-endpoint-storage.md`

## Sources

- [Use private endpoints for Azure Storage](https://learn.microsoft.com/en-us/azure/storage/common/storage-private-endpoints)
- [Azure Private Endpoint private DNS zone values](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns)
