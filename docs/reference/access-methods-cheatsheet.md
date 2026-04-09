---
hide:
  - toc
---

# Access Methods Cheatsheet

Azure Storage supports multiple authorization mechanisms to control data access.

## Comparison Table

| Method | Scope | Expiration | Security | Recommended Use |
| --- | --- | --- | --- | --- |
| Account Key | Storage Account | None | Low | Administrative scripts |
| SAS | Varies by SAS type | Custom | Medium | Temporary client access |
| RBAC | Resource scope (varies by role) | Dynamic | High | Identity-based access to data and resources |
| Managed Identity | Resource | Dynamic | High | Azure-to-Azure communication |
| Anonymous | Container/Blob | None | None | Public assets (e.g. website) |

## Access Method Decision Flow

```mermaid
graph TD
    Start[Access Request] --> Type{Client?}
    Type -->|Azure Resource| MI[Managed Identity]
    Type -->|External App| Auth{Auth Type?}
    Type -->|Browser/Public| Anon[Anonymous]
    
    Auth -->|User Identity| RBAC[Azure RBAC]
    Auth -->|Token Based| SAS[Shared Access Signature]
    Auth -->|Full Admin| Key[Account Key]
```

!!! warning
    Anonymous public read access is disabled by default for new storage accounts. You must explicitly allow public access at the account level before enabling it for containers.

## See Also

- [Access Models](../platform/access-models.md)
- [Security Best Practices](../best-practices/security-best-practices.md)
- [Configure Access and Identity](../operations/configure-access-and-identity.md)

## Sources

- [Authorize access to data in Azure Storage](https://learn.microsoft.com/en-us/azure/storage/common/storage-auth)
- [Grant limited access to Azure Storage resources using SAS](https://learn.microsoft.com/en-us/azure/storage/common/storage-sas-overview)
