# Blob Best Practices

Efficiently manage object storage by selecting correct tiers, naming patterns, and upload strategies.

## Blob Design Decisions

| Consideration | Recommendation |
|---------------|----------------|
| Tier Selection | Match blob tier (Hot, Cool, Cold, Archive) to access frequency. |
| Object Size | Use block blobs for streaming; page blobs for VHDs. |
| Uploading | Use `Put Block` and parallel uploads for large files (>64MB). |
| Immutability | Apply WORM policies for compliance-heavy data. |
| SAS Discipline | Use User Delegation SAS over Service SAS where possible. |
| Naming | Use prefixes for virtual folders (e.g., `logs/2024/04/`). |

## Blob Tier Selection Flow

```mermaid
graph TD
    A[Data Entry] --> B{Accessed Daily?}
    B -->|Yes| C[Hot Tier]
    B -->|No| D{Accessed < 30 Days?}
    D -->|Yes| E[Cool Tier]
    D -->|No| F{Accessed < 90 Days?}
    F -->|Yes| G[Cold Tier]
    F -->|No| H{Compliance/Archive Only?}
    H -->|Yes| I[Archive Tier]
    H -->|No| G
```

!!! note
    **Cold tier** is an online tier with 90-day minimum retention, lower storage cost than Cool but higher access cost. Use it for data accessed less than once per quarter but requiring immediate availability without rehydration.

## See Also

- [Blob Storage Basics](../platform/blob-storage-basics.md)
- [Manage Containers and Shares](../operations/manage-containers-and-shares.md)
- [Lifecycle Management Best Practices](lifecycle-management-best-practices.md)

## Sources

- [Blob Storage best practices](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-introduction)
- [Access tiers overview](https://learn.microsoft.com/en-us/azure/storage/blobs/access-tiers-overview)
- [SAS best practices](https://learn.microsoft.com/en-us/azure/storage/common/storage-sas-overview#best-practices)
