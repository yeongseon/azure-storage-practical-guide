---
description: Performance best practices for Azure Storage covering client placement, partitioning, transfer tuning, and latency review.
content_validation:
  status: verified
  last_reviewed: '2026-07-25'
  reviewer: agent
  core_claims:
    - claim: Blob performance guidance recommends workload-aware partitioning and request shaping.
      source: https://learn.microsoft.com/en-us/azure/storage/blobs/storage-performance-checklist
      verified: true
    - claim: Azure Files workloads should be planned against documented file share scale targets.
      source: https://learn.microsoft.com/en-us/azure/storage/files/storage-files-scale-targets
      verified: true
---

# Performance Best Practices

Use these practices to review Azure Storage performance from latency, concurrency, partition design, and client placement together.

## Why This Matters

Performance tuning fails when teams change SKU or retry settings before identifying the actual bottleneck.

- Latency often comes from region placement, request shape, or prefix hotspots.
- Transfer settings should match real blob sizes and concurrency.
- Premium tiers should follow measured need, not expectation.

## Recommended Practices

- Place compute near storage whenever the architecture allows it.
- Measure object size, request rate, and client distribution before changing SKU.
- Review naming and prefix patterns for partition balance.
- Tune transfer tools only after sampling representative blobs.
- Monitor latency and throttling together, not as separate concerns.

### Example review command

```bash
az monitor metrics list \
    --resource $(az storage account show --resource-group $RG --name $STORAGE_NAME --query id --output tsv) \
    --metric SuccessServerLatency \
    --interval PT1H \
    --output json
```

| Command | Purpose |
| --- | --- |
| `az monitor metrics list` | Pull storage latency data before deciding whether the issue is client-side, network-side, or service-side. |
| `--resource` | Resource ID of the storage account being monitored. |
| `--metric` | Metric name to query, here successful server-side latency. |
| `--interval` | Aggregation interval for the metric query. |
| `--output` | Output format for the result. |

## Common Mistakes / Anti-Patterns

- **Premium by default**: Cost rises before the real cause of latency is proven.
- **Large concurrency without evidence**: More connections can amplify hotspots or throttling.
- **Synthetic test only**: Tiny benchmark files rarely reflect production object layout.

## Validation Checklist

- [ ] Client and storage region placement are reviewed.
- [ ] Request rate and object-size assumptions are measured.
- [ ] Prefix or partition design is sampled.
- [ ] Premium decisions are backed by measured need.
- [ ] Latency and throttling metrics are monitored together.

## See Also

- [Blob Best Practices](blob-best-practices.md)
- [Cost Optimization Best Practices](cost-optimization-best-practices.md)
- [File Share Best Practices](file-share-best-practices.md)

## Sources

- [Performance checklist for Azure Blob Storage](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-performance-checklist)
- [Azure Files scale and performance targets](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-scale-targets)
