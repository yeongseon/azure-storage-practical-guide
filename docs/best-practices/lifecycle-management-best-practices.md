---
description: Lifecycle management best practices for Azure Storage covering rule design, policy execution timing, and safe deletion boundaries.
content_validation:
  status: verified
  last_reviewed: '2026-07-25'
  reviewer: agent
  core_claims:
    - claim: Lifecycle management rules can automatically tier or delete blob data based on conditions.
      source: https://learn.microsoft.com/en-us/azure/storage/blobs/storage-lifecycle-management-concepts
      verified: true
    - claim: Soft delete complements lifecycle rules by enabling recovery of deleted blobs.
      source: https://learn.microsoft.com/en-us/azure/storage/blobs/soft-delete-blob-overview
      verified: true
---

# Lifecycle Management Best Practices

Use these practices to keep lifecycle rules explainable, testable, and safe to operate.

## Why This Matters

Lifecycle automation is powerful, but broad rules can delete or archive data faster than teams realize.

- Prefix and tag design determine whether policy scope is understandable.
- Policy execution is not immediate, so verification matters.
- Destructive lifecycle actions should be paired with recovery controls where needed.

## Recommended Practices

- Translate policy intent into clear prefixes and tags.
- Move data through tiers with timing that reflects business usage, not guesswork.
- Pair delete actions with soft delete, versioning, or backup when recovery still matters.
- Review rule interactions whenever new datasets or prefixes are added.
- Validate policy outcomes with representative blobs after changes.

### Example policy command

```bash
cat > lifecycle-policy.json <<'EOF'
{
  "rules": [
    {
      "enabled": true,
      "name": "archive-old-logs",
      "type": "Lifecycle",
      "definition": {
        "filters": {
          "blobTypes": ["blockBlob"],
          "prefixMatch": ["logs/"]
        },
        "actions": {
          "baseBlob": {
            "tierToCool": { "daysAfterModificationGreaterThan": 30 },
            "tierToArchive": { "daysAfterModificationGreaterThan": 180 },
            "delete": { "daysAfterModificationGreaterThan": 365 }
          }
        }
      }
    }
  ]
}
EOF

az storage account management-policy create \
    --resource-group $RG \
    --account-name $STORAGE_NAME \
    --policy @lifecycle-policy.json \
    --output json
```

| Command | Purpose |
| --- | --- |
| `az storage account management-policy create` | Apply a lifecycle policy after generating the JSON inline in the runbook. |
| `--resource-group` | Resource group that contains the storage account. |
| `--account-name` | Name of the storage account the policy applies to. |
| `--policy` | Path to the JSON policy document created in the previous lines. |
| `--output` | Output format for the result. |

## Common Mistakes / Anti-Patterns

- **Rules nobody can explain**: If operators cannot say which prefixes a rule affects, it is too broad.
- **Delete first, recover later**: Recovery controls should be agreed before destructive automation is enabled.
- **Control-plane success only**: A policy that saves successfully still needs blob-level validation later.

## Validation Checklist

- [ ] Prefixes or tags clearly define policy scope.
- [ ] Tier timing reflects real business access patterns.
- [ ] Delete rules are paired with recovery controls where appropriate.
- [ ] Policy changes are reviewed for interaction with existing rules.
- [ ] Sample blobs are validated after policy updates.

## See Also

- [Cost Optimization Best Practices](cost-optimization-best-practices.md)
- [Blob Best Practices](blob-best-practices.md)
- [Common Anti-Patterns](common-anti-patterns.md)

## Sources

- [Azure Blob Storage lifecycle management overview](https://learn.microsoft.com/en-us/azure/storage/blobs/lifecycle-management-overview)
- [Soft delete for blobs](https://learn.microsoft.com/en-us/azure/storage/blobs/soft-delete-blob-overview)
