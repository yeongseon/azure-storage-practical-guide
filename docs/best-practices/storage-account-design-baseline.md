---
description: Production baseline for Azure Storage account design covering account type, redundancy, network exposure, diagnostics, and ownership defaults.
content_validation:
  status: verified
  last_reviewed: '2026-07-25'
  reviewer: agent
  core_claims:
    - claim: Azure Storage offers several storage account types, and Microsoft recommends standard general-purpose v2 accounts for most scenarios.
      source: https://learn.microsoft.com/en-us/azure/storage/common/storage-account-overview
      verified: true
    - claim: Azure Storage redundancy guidance says you should choose a redundancy option by weighing lower cost against higher availability.
      source: https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy
      verified: true
---

# Storage Account Design Baseline

Use this baseline to standardize how new Azure Storage accounts are created before workload-specific tuning begins.

## Why This Matters

Most storage incidents come from inconsistent defaults rather than from a missing platform feature.

- Teams create different network, TLS, and access settings for similar workloads.
- Ownership gaps make lifecycle, backup, and cost exceptions hard to review later.
- Ad hoc account choices lead to avoidable migration work when a workload grows.

## Recommended Practices

- Start with **general-purpose v2** unless a measured requirement justifies a premium or specialized account type.
- Decide redundancy from business recovery requirements, not from habit.
- Disable unnecessary public exposure and record any approved exceptions.
- Require named owners for security, lifecycle, backup, and cost decisions.
- Turn on diagnostics before application cutover so the first incident has evidence.

### Example review command

```bash
az storage account show \
    --resource-group $RG \
    --name $STORAGE_NAME \
    --query "{kind:kind,sku:sku.name,minimumTlsVersion:minimumTlsVersion,publicNetworkAccess:publicNetworkAccess,allowBlobPublicAccess:allowBlobPublicAccess,allowSharedKeyAccess:allowSharedKeyAccess}" \
    --output json
```

| Command | Purpose |
| --- | --- |
| `az storage account show` | Export the baseline settings that should be reviewed before approving a new storage account. |
| `--resource-group` | Resource group that contains the storage account. |
| `--name` | Name of the storage account to inspect. |
| `--query` | JMESPath expression selecting baseline design fields. |
| `--output` | Output format for the result. |

## Common Mistakes / Anti-Patterns

- **One default for every workload**: Blob, file share, and analytics workloads do not all need the same account design.
- **Redundancy without rationale**: Paying for geo-redundancy without a failover plan is wasteful, while using LRS for regional recovery goals is unsafe.
- **Security added later**: Leaving public access, Shared Key, or weak TLS defaults in place creates cleanup work after data already exists.

## Validation Checklist

- [ ] Account kind is explicitly justified.
- [ ] Redundancy matches documented RPO and RTO expectations.
- [ ] Public network exposure and Shared Key posture are reviewed.
- [ ] Diagnostic settings are enabled or an exception is documented.
- [ ] Ownership for lifecycle, backup, and cost decisions is recorded.

## See Also

- [Blob Best Practices](blob-best-practices.md)
- [Security Best Practices](security-best-practices.md)
- [Redundancy and DR Best Practices](redundancy-and-dr-best-practices.md)

## Sources

- [Storage account overview](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-overview)
- [Azure Storage redundancy](https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy)
