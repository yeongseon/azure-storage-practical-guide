---
description: Common Azure Storage anti-patterns to detect early, including mixed-purpose accounts, broad access paths, weak tiering logic, and unclear ownership.
content_validation:
  status: verified
  last_reviewed: '2026-07-25'
  reviewer: agent
  core_claims:
    - claim: Blob security guidance says Microsoft Entra ID is more secure than Shared Key and recommends firewall or private endpoint controls.
      source: https://learn.microsoft.com/en-us/azure/storage/blobs/security-recommendations
      verified: true
    - claim: Lifecycle management guidance says policies can move blobs to cooler tiers or delete them, so those rules should match real data access patterns.
      source: https://learn.microsoft.com/en-us/azure/storage/blobs/lifecycle-management-overview
      verified: true
---

# Common Anti-Patterns

Use this page to catch recurring Azure Storage design mistakes before they turn into incidents, audit gaps, or runaway cost.

## Why This Matters

Anti-patterns are usually visible early, but they are easy to normalize when teams optimize for speed over clarity.

- Mixed-purpose accounts blur ownership and blast radius.
- Broad access paths stay in place long after the original shortcut is forgotten.
- Tiering and lifecycle mistakes compound over time because the data keeps growing.

## Recommended Practices

- Split workloads by security boundary, access pattern, and lifecycle ownership.
- Treat Shared Key and broad SAS usage as exceptions that need review.
- Review public network exposure and firewall exceptions together.
- Validate tiering choices with actual access patterns and recovery expectations.
- Keep operational ownership explicit for backup, lifecycle, and cost decisions.

### Example review command

```bash
az storage account show \
    --resource-group $RG \
    --name $STORAGE_NAME \
    --query "{publicNetworkAccess:publicNetworkAccess,allowSharedKeyAccess:allowSharedKeyAccess,accessTier:accessTier,sku:sku.name}" \
    --output json
```

| Command | Purpose |
| --- | --- |
| `az storage account show` | Surface the control settings that most often reveal storage anti-patterns. |
| `--resource-group` | Resource group that contains the storage account. |
| `--name` | Name of the storage account to inspect. |
| `--query` | JMESPath expression selecting high-signal anti-pattern indicators. |
| `--output` | Output format for the result. |

## Common Mistakes / Anti-Patterns

- **One account for every workload**: Shared boundaries make lifecycle, network, and permission decisions conflict.
- **Long-lived broad access**: Shared Key, wide SAS, and public paths accumulate risk quietly.
- **Uniform tiering**: Hot and archival data should not automatically share the same retention logic.

## Validation Checklist

- [ ] Workloads are separated by security or lifecycle boundary where needed.
- [ ] Shared Key and SAS usage are reviewed and justified.
- [ ] Public network exposure is intentionally configured.
- [ ] Tiering and lifecycle rules match real access patterns.
- [ ] Ownership for operations and exceptions is explicit.

## See Also

- [Storage Account Design Baseline](storage-account-design-baseline.md)
- [Security Best Practices](security-best-practices.md)
- [Lifecycle Management Best Practices](lifecycle-management-best-practices.md)

## Sources

- [Security recommendations for Blob Storage](https://learn.microsoft.com/en-us/azure/storage/blobs/security-recommendations)
- [Azure Blob Storage lifecycle management overview](https://learn.microsoft.com/en-us/azure/storage/blobs/lifecycle-management-overview)
