# SAS and Token Issues

Resolve authentication and validation failures with Shared Access Signatures.

| SAS Failure | Cause | Resolution |
|-------------|-------|------------|
| Expired | Start/Expiry date | Re-generate SAS. |
| Clock Skew | Client/Server sync | Use +/- 15m buffer. |
| Wrong Permission | Missing 'r/w/d' | Check SAS definition. |
| Path Scope | SAS on wrong container | Re-generate at correct scope. |
| Service Mix | Service SAS vs Account SAS | Use appropriate SAS type. |

```mermaid
graph TD
    A[SAS Error] --> B{Expired?}
    B -->|Yes| C[Regenerate SAS]
    B -->|No| D{Right Permissions?}
    D -->|No| E[Check SAS string]
    D -->|Yes| F[Check Storage Firewall]
```

## Sources
- [Shared Access Signatures overview](https://learn.microsoft.com/en-us/azure/storage/common/storage-sas-overview)
- [Troubleshoot SAS errors](https://learn.microsoft.com/en-us/azure/storage/common/storage-sas-overview#best-practices)
