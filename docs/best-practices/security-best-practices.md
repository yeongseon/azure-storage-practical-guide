---
description: Security best practices for Azure Storage covering Entra authorization, Shared Key reduction, telemetry, encryption review, and private access posture.
content_validation:
  status: verified
  last_reviewed: '2026-07-25'
  reviewer: agent
  core_claims:
    - claim: Microsoft recommends preferring Microsoft Entra authorization for Azure Storage data access when possible.
      source: https://learn.microsoft.com/en-us/azure/storage/common/storage-security-guide
      verified: true
    - claim: Blob security guidance includes least privilege, network restriction, and data protection controls.
      source: https://learn.microsoft.com/en-us/azure/storage/blobs/security-recommendations
      verified: true
---

# Security Best Practices

Use these practices to reduce unnecessary exposure in Azure Storage and keep access decisions auditable.

## Why This Matters

Storage accounts concentrate valuable data, so weak defaults quickly become broad blast-radius problems.

- Shared Key and broad SAS links are hard to track and revoke.
- Public network exposure increases exfiltration risk.
- Missing telemetry turns simple incidents into lengthy investigations.

## Recommended Practices

- Make Microsoft Entra ID and RBAC the default for people and automation.
- Treat SAS as a short-lived exception with narrow scope and expiry.
- Disable unnecessary public access paths and validate private connectivity.
- Turn on diagnostics before data is onboarded.
- Review encryption posture together with network and identity posture.

### Example review commands

```bash
az storage account show \
    --resource-group $RG \
    --name $STORAGE_NAME \
    --query "{publicNetworkAccess:publicNetworkAccess,allowBlobPublicAccess:allowBlobPublicAccess,allowSharedKeyAccess:allowSharedKeyAccess,minimumTlsVersion:minimumTlsVersion}" \
    --output json

az monitor diagnostic-settings list \
    --resource $(az storage account show --resource-group $RG --name $STORAGE_NAME --query id --output tsv) \
    --output json
```

| Command | Purpose |
| --- | --- |
| `az storage account show` | Review the account's exposed access controls before approving production use. |
| `--resource-group` | Resource group that contains the storage account. |
| `--name` | Name of the storage account to inspect. |
| `--query` | JMESPath expression selecting the most important security fields. |
| `--output` | Output format for the result. |
| `az monitor diagnostic-settings list` | Confirm whether storage logs and metrics are already flowing to a monitoring destination. |
| `--resource` | Resource ID of the storage account being inspected. |
| `--output` | Output format for the result. |

## Common Mistakes / Anti-Patterns

- **Shared Key kept as the default**: Convenience today becomes invisible long-lived risk later.
- **Security without evidence**: Claims about secure posture are weak if logs and metrics are disabled.
- **Encryption discussed alone**: Key management choices should be reviewed with identity and network controls, not in isolation.

## Validation Checklist

- [ ] Microsoft Entra ID and RBAC are preferred over Shared Key.
- [ ] Public access posture is reviewed and justified.
- [ ] Diagnostic settings are enabled or an exception is documented.
- [ ] SAS issuance rules are short-lived and least-privilege.
- [ ] Encryption posture is reviewed with the wider access model.

## See Also

- [Networking Best Practices](networking-best-practices.md)
- [Common Anti-Patterns](common-anti-patterns.md)
- [Blob Best Practices](blob-best-practices.md)

## Sources

- [Security recommendations for Blob Storage](https://learn.microsoft.com/en-us/azure/storage/blobs/security-recommendations)
- [Security guide for Azure Storage](https://learn.microsoft.com/en-us/azure/storage/common/storage-security-guide)
