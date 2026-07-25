---
content_sources:
  diagrams:
    - id: platform-blob-storage-basics
      type: flowchart
      source: mslearn-adapted
      mslearn_url: https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-introduction
content_validation:
  status: pending_review
  last_reviewed: '2026-07-25'
  reviewer: agent
  core_claims:
    - claim: Azure Blob Storage stores massive amounts of unstructured object data in containers.
      source: https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-introduction
      verified: false
    - claim: Blob data supports access tiers such as hot, cool, and archive for different access patterns.
      source: https://learn.microsoft.com/en-us/azure/storage/blobs/access-tiers-overview
      verified: false
---

# Blob Storage Basics

Blob Storage is Azure's object storage solution for the cloud, optimized for storing massive amounts of unstructured data.

| Tier | Availability | Cost (Storage) | Cost (Access) | Retention |
| :--- | :--- | :--- | :--- | :--- |
| **Hot** | Highest | Highest | Lowest | None |
| **Cool** | High | Low | High | 30 days |
| **Cold** | Medium | Lower | Higher | 90 days |
| **Archive** | Lowest | Lowest | Highest | 180 days |

<!-- diagram-id: platform-blob-storage-basics -->
```mermaid
graph TD
    H[Hot Tier] -- Frequent --> C[Cool Tier]
    C -- Infrequent --> CL[Cold Tier]
    CL -- Rare --> A[Archive Tier]
    A -- Rehydrate --> H
    H -- Delete --> D((Deleted))
```

## Storage Concepts
- **Containers**: Groups of blobs, similar to a directory in a file system.
- **Blobs**: Individual data objects (Block, Page, or Append).
- **Metadata**: Key-value pairs associated with a blob or container.

## Data Types
- **Block Blobs**: Best for documents, images, and videos.
- **Append Blobs**: Optimized for logging operations.
- **Page Blobs**: Designed for frequent random read/write operations (e.g., VHDs).

!!! tip
    Define access tiers and lifecycle policies together so data moves predictably between Hot, Cool, Cold, and Archive based on age and access frequency.

## See Also

- [Blob Best Practices](../best-practices/blob-best-practices.md)
- [Manage Containers and Shares](../operations/manage-containers-and-shares.md)
- [Access Models](access-models.md)

## Sources
- [Introduction to Azure Blob Storage](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-introduction)
- [Access tiers for blob data](https://learn.microsoft.com/en-us/azure/storage/blobs/access-tiers-overview)
