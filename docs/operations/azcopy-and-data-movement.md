# AzCopy and Data Movement

Perform high-performance data transfers to and from Azure Storage.

| Tool | Format | Ideal Data Volume |
|------|--------|-------------------|
| AzCopy | Command Line | GB to TB |
| Storage Explorer | GUI | MB to GB |
| Data Box | Physical Device | 40TB to PB |
| Azure Portal | Web Interface | KB to MB |

!!! note
    AzCopy supports both Shared Access Signatures (SAS) and Azure Active Directory (Azure AD) for authentication.

```mermaid
graph TD
    A[Data Source] --> B{Data Size?}
    B -->|Small| C[Portal / Explorer]
    B -->|Large| D[AzCopy]
    B -->|Massive| E[Azure Data Box]
    C --> F[Azure Storage]
    D --> F
    E --> F
```

## Sources
- [Get started with AzCopy](https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10)
- [Move data with Azure Data Box](https://learn.microsoft.com/en-us/azure/databox/data-box-overview)
