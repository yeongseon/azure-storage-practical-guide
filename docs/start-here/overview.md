---
content_sources:
  diagrams:
    - id: start-here-overview
      type: flowchart
      source: mslearn-adapted
      mslearn_url: https://learn.microsoft.com/en-us/azure/storage/common/storage-introduction
---

# Overview

Azure Storage is the foundational data service for Microsoft Azure. Most Azure services depend on it for data persistence, application state, and durability.

## Core Storage Services

| Service | Best For |
| ------- | -------- |
| Blob Storage | Unstructured data (objects, images, documents) |
| Azure Files | Fully managed cloud file shares (SMB/NFS) |
| Queue Storage | Asynchronous message queueing |
| Table Storage | NoSQL key-value store |
| Blob Storage with Data Lake Storage Gen2 | Big data analytics with hierarchical namespace |

## Service Hierarchy

<!-- diagram-id: start-here-overview -->
```mermaid
graph TD
    SA[Storage Account]
    SA --> BS[Blob Storage]
    SA --> AF[Azure Files]
    SA --> QS[Queue Storage]
    SA --> TS[Table Storage]
    BS --> DL[Data Lake Storage Gen2]
```

!!! note
    The Storage Account is the unique namespace and common foundation for all storage services. Account-level settings like redundancy apply broadly, but the default access tier applies only to Blob Storage in supported account types.

## Scope of this Guide

- Included: Cloud-native storage services, data redundancy, security patterns.
- Excluded: Compute-attached storage, SQL databases, Cosmos DB.

## See Also

- [How Azure Storage Works](../platform/how-azure-storage-works.md)
- [Common Scenarios](common-scenarios.md)
- [Storage Service Selection Guide](../reference/storage-service-selection-guide.md)

## Sources

- [Introduction to Azure Storage](https://learn.microsoft.com/en-us/azure/storage/common/storage-introduction)
- [About Azure Storage accounts](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-overview)
