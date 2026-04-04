# Storage Service Selection Guide

Choosing the right storage service depends on data structure, access protocols, and performance requirements.

## Workload to Service Mapping

| Workload | Recommended Service | Data Type | Protocol | Scale |
| --- | --- | --- | --- | --- |
| Web assets, Big Data, Backup | Blob Storage | Unstructured | REST/HDFS | PB+ |
| Shared file systems (Lift & Shift) | Azure Files | SMB/NFS | SMB/NFS/REST | 100TiB+ |
| VM OS and Data Disks | Azure Managed Disks | Block | SCSI/NVMe | 64TiB |
| High-volume messaging | Azure Queues | Messages | REST | Account limit |
| NoSQL key-value storage | Azure Tables | Structured | REST | Account limit |
| Large-scale analytics | Data Lake Storage Gen2 | Hierarchical | HDFS/REST | PB+ |

## Selection Decision Tree

```mermaid
graph TD
    Start[New Workload] --> Unstruct{Data Type?}
    Unstruct -->|Unstructured| Access{Access Method?}
    Unstruct -->|Structured| NoSQL[Azure Tables]
    Unstruct -->|Messages| Queue[Azure Queues]
    
    Access -->|REST API| Blobs[Azure Blob Storage]
    Access -->|Shared File| Protocol{Protocol?}
    Access -->|VM Disk| Disks[Managed Disks]
    
    Protocol -->|SMB/NFS| Files[Azure Files]
    Protocol -->|HDFS| ADLS[Data Lake Storage Gen2]
```

!!! tip
    Use Azure Files for shared application data when multiple VMs need concurrent access to the same file system without rewriting code.

## Sources

- [Choose an Azure storage service](https://learn.microsoft.com/en-us/azure/storage/common/storage-introduction#azure-storage-services)
- [Review your storage options](https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/data-store-overview)
