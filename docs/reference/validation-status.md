---
content_sources:
  diagrams:
    - id: reference-validation-status
      type: pie
      source: self-generated
      justification: "Repository validation summary generated from local tutorial validation metadata."
      based_on:
        - https://learn.microsoft.com/en-us/azure/storage/
---

# Tutorial Validation Status

This page tracks which lab guides have been validated against real Azure deployments. Each guide can be tested via **az-cli** (manual CLI commands) or **Bicep** (infrastructure as code). Guides not tested within 90 days are marked as stale.

## Summary

*Generated: 2026-04-09*

| Metric | Count |
|---|---:|
| Total lab guides | 5 |
| ✅ Validated | 0 |
| ⚠️ Stale (>90 days) | 0 |
| ❌ Failed | 0 |
| ➖ Not tested | 5 |

<!-- diagram-id: reference-validation-status -->
```mermaid
pie title Tutorial Validation Status
    "Not Tested" : 5
```

## Validation Matrix

| Lab Guide | az-cli | Bicep | Last Tested | Status |
|---|---|---|---|---|
| [Lab 01 Blob Lifecycle Management](../tutorials/lab-guides/lab-01-blob-lifecycle-management.md) | ➖ No Data | ➖ No Data | — | ➖ Not Tested |
| [Lab 02 Private Endpoint Storage](../tutorials/lab-guides/lab-02-private-endpoint-storage.md) | ➖ No Data | ➖ No Data | — | ➖ Not Tested |
| [Lab 03 Azure File Share Ad Integration](../tutorials/lab-guides/lab-03-azure-file-share-ad-integration.md) | ➖ No Data | ➖ No Data | — | ➖ Not Tested |
| [Lab 04 Storage Replication Failover](../tutorials/lab-guides/lab-04-storage-replication-failover.md) | ➖ No Data | ➖ No Data | — | ➖ Not Tested |
| [Lab 05 Static Website Cdn](../tutorials/lab-guides/lab-05-static-website-cdn.md) | ➖ No Data | ➖ No Data | — | ➖ Not Tested |

## How to Update

To mark a lab guide as validated, add a `validation` block to its YAML frontmatter:

```yaml
---
validation:
  az_cli:
    last_tested: 2026-04-09
    cli_version: "2.83.0"
    result: pass
  bicep:
    last_tested: null
    result: not_tested
---
```

Then regenerate this page:

```bash
python3 scripts/generate_validation_status.py
```

!!! info "Validation fields"
    - `result`: `pass`, `fail`, or `not_tested`
    - `last_tested`: ISO date (YYYY-MM-DD) or `null`
    - `cli_version`: Azure CLI version used
    - Lab guides older than 90 days are flagged as **stale**

## See Also

- [Tutorials](../tutorials/index.md)
- [Lab Guides](../tutorials/lab-guides/index.md)
- [Storage Service Selection Guide](storage-service-selection-guide.md)

