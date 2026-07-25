---
description: Best practices for Azure Storage redundancy and disaster recovery covering replication choice, failover review, and secondary-region readiness.
content_validation:
  status: verified
  last_reviewed: '2026-07-25'
  reviewer: agent
  core_claims:
    - claim: Azure Storage disaster recovery guidance says the replication option you choose determines the level of resiliency your application gets.
      source: https://learn.microsoft.com/en-us/azure/storage/common/storage-disaster-recovery-guidance
      verified: true
    - claim: Geo-redundancy design guidance says RA-GRS and RA-GZRS provide read access to the secondary region.
      source: https://learn.microsoft.com/en-us/azure/storage/common/geo-redundant-design
      verified: true
---

# Redundancy and DR Best Practices

Use these practices to tie redundancy cost to a clear failover decision model and documented recovery expectations.

## Why This Matters

Replication helps only when teams understand what a given mode covers and what it does not.

- LRS, ZRS, GRS, and RA-GZRS solve different failure scenarios.
- Secondary-read capability changes application design and testing needs.
- Backup, replication, and failover communications should not be treated as the same control.

## Recommended Practices

- Choose redundancy from business RPO and RTO, not from naming familiarity.
- Test application behavior for secondary reads and manual failover paths.
- Keep backup and replication decisions separate in runbooks.
- Record who can authorize failover and how stakeholders are informed.
- Review last sync time before any manual failover decision.

### Example review command

```bash
az storage account show \
    --resource-group $RG \
    --name $STORAGE_NAME \
    --query "{sku:sku.name,primaryLocation:primaryLocation,secondaryLocation:secondaryLocation,lastSyncTime:lastSyncTime,statusOfPrimary:statusOfPrimary,statusOfSecondary:statusOfSecondary}" \
    --output json
```

| Command | Purpose |
| --- | --- |
| `az storage account show` | Capture the failover-relevant fields that should be reviewed before a DR drill or outage decision. |
| `--resource-group` | Resource group that contains the storage account. |
| `--name` | Name of the storage account to inspect. |
| `--query` | JMESPath expression selecting redundancy and replication-status fields. |
| `--output` | Output format for the result. |

## Common Mistakes / Anti-Patterns

- **Replication treated as backup**: Replicated corruption is still corruption.
- **Geo-redundancy without testing**: Paying for a secondary region is not the same as knowing how to use it.
- **Failover without communications**: Technical recovery steps fail when ownership and messaging are unclear.

## Validation Checklist

- [ ] Redundancy maps to a documented outage model.
- [ ] Secondary-read behavior is understood where applicable.
- [ ] Backup and replication plans are separated.
- [ ] Failover authority and communication steps are documented.
- [ ] Last sync time is part of outage review.

## See Also

- [Storage Account Design Baseline](storage-account-design-baseline.md)
- [Cost Optimization Best Practices](cost-optimization-best-practices.md)
- [Networking Best Practices](networking-best-practices.md)

## Sources

- [Azure storage disaster recovery planning and failover](https://learn.microsoft.com/en-us/azure/storage/common/storage-disaster-recovery-guidance)
- [Use geo-redundancy to design highly available applications](https://learn.microsoft.com/en-us/azure/storage/common/geo-redundant-design)
