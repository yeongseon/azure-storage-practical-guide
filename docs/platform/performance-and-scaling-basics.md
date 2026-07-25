---
content_sources:
  diagrams:
    - id: platform-performance-and-scaling-basics
      type: flowchart
      source: mslearn-adapted
      mslearn_url: https://learn.microsoft.com/en-us/azure/storage/common/scalability-targets-standard-account
content_validation:
  status: pending_review
  last_reviewed: '2026-07-25'
  reviewer: agent
  core_claims:
    - claim: Standard storage accounts have documented scalability targets for capacity and throughput.
      source: https://learn.microsoft.com/en-us/azure/storage/common/scalability-targets-standard-account
      verified: false
    - claim: Blob performance guidance emphasizes partition-aware naming and request distribution.
      source: https://learn.microsoft.com/en-us/azure/storage/blobs/storage-performance-checklist
      verified: false
---

# Performance and Scaling Basics

Understanding performance limits and scaling targets is essential for designing efficient Azure Storage solutions.

| Metric | Standard Account | Premium Block Blob | Premium File Share |
| :--- | :--- | :--- | :--- |
| **Request Rate** | Up to 40,000 requests/sec (default in listed regions); 20,000 requests/sec in other regions | Service-specific premium targets (see source) | Up to 102,400 (provisioned SSD) |
| **Ingress** | Up to 60 Gbps (default in listed regions); 25 Gbps in other regions | Service-specific premium targets (see source) | Service/account-level throughput targets apply |
| **Egress** | Up to 200 Gbps (default in listed regions); 50 Gbps in other regions | Service-specific premium targets (see source) | Service/account-level throughput targets apply |
| **Capacity** | 5 PiB per account (default) | Service-specific premium targets (see source) | Up to 256 TiB (provisioned v2) |

<!-- diagram-id: platform-performance-and-scaling-basics -->
```mermaid
graph TD
    App[App Request] --> Th{Throttled?}
    Th -- Yes --> Client{Client Action}
    Client --> Parallel[Increase Parallelism]
    Client --> Retry[Exponential Backoff]
    Th -- No --> Partition[Partition Check]
    Partition --> Key[Optimize Partition Key]
    Key --> Success[High Throughput]
```

!!! note
    Limits are region-dependent and workload-dependent. Higher capacity and ingress/egress limits can be requested through Azure Support. See the [Microsoft Learn source](https://learn.microsoft.com/en-us/azure/storage/common/scalability-targets-standard-account) for the current list of regions that receive the higher default targets.

## Key Concepts
- **Throughput**: The amount of data transferred per second.
- **IOPS**: The number of input/output operations per second.
- **Partitioning**: Azure Storage uses a partition key to scale data across multiple servers.

## See Also

- [Performance Best Practices](../best-practices/performance-best-practices.md)
- [Performance Terms](../reference/performance-terms.md)
- [Blob Storage Basics](blob-storage-basics.md)

## Sources
- [Azure Storage scalability and performance targets](https://learn.microsoft.com/en-us/azure/storage/common/scalability-targets-standard-account)
- [Performance and scalability checklist for Blob storage](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-performance-checklist)
