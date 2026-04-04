# Throttling and Performance Issues

Address HTTP 503 and 429 errors caused by storage limits.

| Throttling Indicator | Metric | Resolution |
|----------------------|--------|------------|
| HTTP 503 Server Busy | ServerLatency | Retry with backoff. |
| HTTP 429 Too Many Req| SuccessPercentage | Distribute traffic. |
| Latency Spikes | E2E Latency | Check parallelism. |
| Retry Patterns | Transaction count | Scale-out storage accounts. |

!!! note
    Azure Storage is designed to handle high load, but extreme spikes may trigger defensive throttling.

```mermaid
graph TD
    A[Error 503/429] --> B{Account Limits?}
    B -->|Yes| C[Distribute Load]
    B -->|No| D{Parallelism High?}
    D -->|Yes| E[Reduce Concurrent Req]
    D -->|No| F[Retry with Backoff]
```

## Sources
- [Scalability and performance targets](https://learn.microsoft.com/en-us/azure/storage/common/storage-scalability-targets)
- [Storage throttling overview](https://learn.microsoft.com/en-us/azure/storage/common/storage-throttling-errors)
