---
content_sources:
  diagrams:
    - id: tutorials-lab-guides-lab-02-private-endpoint-storage
      type: flowchart
      source: mslearn-adapted
      mslearn_url: https://learn.microsoft.com/en-us/azure/storage/common/storage-private-endpoints
---

# Lab 02: Private Endpoint for Storage

Deploy a storage account with a Private Endpoint and Private DNS Zone, then validate that traffic resolves and reaches the service privately.

## Prerequisites

- Azure subscription with permission to create storage, networking, and monitoring resources.
- Azure CLI logged in with the correct tenant and subscription.
- Variables defined for `$RG`, `$LOCATION`, `$STORAGE_NAME`, and any lab-specific names.
- A workstation or Cloud Shell session with access to the resource group.
- Optional Log Analytics workspace if you want to capture diagnostics during the lab.

## Architecture Diagram

<!-- diagram-id: tutorials-lab-guides-lab-02-private-endpoint-storage -->
```mermaid
flowchart TD
    A[Operator workstation] --> B[Azure CLI]
    B --> C[Resource group]
    C --> D[Storage account]
    D --> E[Data path under test]
    D --> F[Lifecycle, networking, or replication control]
    D --> G[Validation and cleanup]
```

## Step-by-Step Instructions

### Step 1: Create the storage account and virtual network

```bash
az storage account create \
    --resource-group $RG \
    --name $STORAGE_NAME \
    --location $LOCATION \
    --sku Standard_ZRS \
    --kind StorageV2 \
    --public-network-access Disabled \
    --output json

az network vnet create \
    --resource-group $RG \
    --name $VNET_NAME \
    --address-prefixes 10.40.0.0/16 \
    --subnet-name $SUBNET_NAME \
    --subnet-prefixes 10.40.1.0/24 \
    --output json
```

| Command | Purpose |
| --- | --- |
| `az storage account create` | Create a storage account with the public endpoint disabled. |
| `--resource-group` | Resource group that will contain the account. |
| `--name` | Globally unique name of the storage account. |
| `--location` | Azure region for the account. |
| `--sku` | Redundancy tier, zone-redundant Standard (`Standard_ZRS`). |
| `--kind` | Account kind, `StorageV2` for general-purpose v2. |
| `--public-network-access` | Disable the public endpoint when `Disabled`. |
| `--output` | Output format for the result. |
| `az network vnet create` | Create a virtual network with an initial subnet. |
| `--resource-group` | Resource group that will contain the virtual network. |
| `--name` | Name of the virtual network to create. |
| `--address-prefixes` | Address space of the virtual network. |
| `--subnet-name` | Name of the initial subnet. |
| `--subnet-prefixes` | Address range of the initial subnet. |
| `--output` | Output format for the result. |


- Record the output and any IDs you will reuse in later steps.
- If the command creates security-sensitive settings, confirm they match policy before moving on.
- Capture screenshots or JSON output for your lab notes if you are building internal training material.
### Step 2: Create the Private DNS Zone and link the VNet

```bash
az network private-dns zone create \
    --resource-group $RG \
    --name privatelink.blob.core.windows.net \
    --output json

az network private-dns link vnet create \
    --resource-group $RG \
    --zone-name privatelink.blob.core.windows.net \
    --name storage-link \
    --virtual-network $(az network vnet show --resource-group $RG --name $VNET_NAME --query id --output tsv) \
    --registration-enabled false \
    --output json
```

| Command | Purpose |
| --- | --- |
| `az network private-dns zone create` | Create a private DNS zone for blob private endpoints. |
| `--resource-group` | Resource group that will contain the zone. |
| `--name` | Zone name (`privatelink.blob.core.windows.net`). |
| `--output` | Output format for the result. |
| `az network private-dns link vnet create` | Link the private DNS zone to a virtual network. |
| `--resource-group` | Resource group that contains the private DNS zone. |
| `--zone-name` | Name of the private DNS zone to link. |
| `--name` | Name of the virtual network link to create. |
| `--virtual-network` | Resource ID of the virtual network to link. |
| `--registration-enabled` | Disable auto-registration of VM records when `false`. |
| `--output` | Output format for the result. |


- Record the output and any IDs you will reuse in later steps.
- If the command creates security-sensitive settings, confirm they match policy before moving on.
- Capture screenshots or JSON output for your lab notes if you are building internal training material.
### Step 3: Create the Private Endpoint

```bash
az network private-endpoint create \
    --resource-group $RG \
    --name $PRIVATE_ENDPOINT_NAME \
    --vnet-name $VNET_NAME \
    --subnet $SUBNET_NAME \
    --private-connection-resource-id $(az storage account show --resource-group $RG --name $STORAGE_NAME --query id --output tsv) \
    --group-id blob \
    --connection-name storage-blob-connection \
    --output json
```

| Command | Purpose |
| --- | --- |
| `az network private-endpoint create` | Create a private endpoint for the storage account. |
| `--resource-group` | Resource group that will contain the private endpoint. |
| `--name` | Name of the private endpoint. |
| `--vnet-name` | Virtual network that hosts the private endpoint subnet. |
| `--subnet` | Subnet in which the private endpoint IP is allocated. |
| `--private-connection-resource-id` | Resource ID of the storage account being connected. |
| `--group-id` | Target sub-resource of the account (`blob`). |
| `--connection-name` | Name of the private link connection. |
| `--output` | Output format for the result. |


- Record the output and any IDs you will reuse in later steps.
- If the command creates security-sensitive settings, confirm they match policy before moving on.
- Capture screenshots or JSON output for your lab notes if you are building internal training material.
### Step 4: Create the DNS zone group

```bash
az network private-endpoint dns-zone-group create \
    --resource-group $RG \
    --endpoint-name $PRIVATE_ENDPOINT_NAME \
    --name default \
    --private-dns-zone privatelink.blob.core.windows.net \
    --zone-name privatelink.blob.core.windows.net \
    --output json
```

| Command | Purpose |
| --- | --- |
| `az network private-endpoint dns-zone-group create` | Associate a private DNS zone with the private endpoint. |
| `--resource-group` | Resource group that contains the private endpoint. |
| `--endpoint-name` | Name of the private endpoint to configure. |
| `--name` | Name of the DNS zone group (`default`). |
| `--private-dns-zone` | Private DNS zone to associate. |
| `--zone-name` | Zone name key used within the group. |
| `--output` | Output format for the result. |


- Record the output and any IDs you will reuse in later steps.
- If the command creates security-sensitive settings, confirm they match policy before moving on.
- Capture screenshots or JSON output for your lab notes if you are building internal training material.

## Validation Steps

1. Confirm the storage account properties match the intended SKU, kind, and access posture.
2. Validate the lab-specific feature from the consumer point of view rather than trusting only control-plane success.
3. Capture one or more JSON outputs that prove the configuration is active.
4. Record any timing behavior that matters, especially for lifecycle or replication scenarios.
5. Note the operational follow-up required before using the same pattern in production.

### Example validation commands

```bash
az storage account show \
    --resource-group $RG \
    --name $STORAGE_NAME \
    --output json
```

| Command | Purpose |
| --- | --- |
| `az storage account show` | Show full properties of the storage account. |
| `--resource-group` | Resource group that contains the account. |
| `--name` | Name of the storage account to inspect. |
| `--output` | Output format for the result. |


```bash
az monitor diagnostic-settings list \
    --resource $(az storage account show --resource-group $RG --name $STORAGE_NAME --query id --output tsv) \
    --output json
```

| Command | Purpose |
| --- | --- |
| `az monitor diagnostic-settings list` | List diagnostic settings configured on a resource. |
| `--resource` | Resource ID being inspected, here the storage account. |
| `--output` | Output format for the result. |


## Cleanup Instructions

- Delete lab resources when validation is complete to prevent ongoing cost.
- Preserve any JSON output or screenshots you need before deletion.
- If you created role assignments or network links used elsewhere, confirm scope before removing them.

```bash
az group delete \
    --name $RG \
    --yes \
    --no-wait
```

| Command | Purpose |
| --- | --- |
| `az group delete` | Delete a resource group and all resources in it. |
| `--name` | Name of the resource group to delete. |
| `--yes` | Skip the interactive confirmation prompt. |
| `--no-wait` | Return immediately without waiting for deletion to finish. |


## See Also

- [Networking Best Practices](../../best-practices/networking-best-practices.md)
- [Use Private Endpoints](../../operations/use-private-endpoints.md)
- [Blob Access Denied](../../troubleshooting/playbooks/blob-access-denied.md)

## Sources

- [azure/storage/common/storage-private-endpoints](https://learn.microsoft.com/en-us/azure/storage/common/storage-private-endpoints)
- [azure/storage/common/storage-network-security](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security)
