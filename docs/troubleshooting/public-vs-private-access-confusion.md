# Public vs Private Access Confusion

Resolve confusion between public and private network access.

| Scenario | Behavior | Diagnosis |
|----------|----------|-----------|
| No Access | Public off, no PE | Network path is blocked. |
| Resolves Public | PE exists, DNS public IP | DNS zone link missing. |
| Firewalled | Firewall + DNS mismatch | Add client IP or use PE. |
| Mixed Access | PE exists, Public on | Traffic routes by DNS. |

!!! tip
    Always check DNS resolution first to see which endpoint (public vs private) the client is trying to reach.

```mermaid
graph TD
    A[Access Issue] --> B{Resolved IP?}
    B -->|Public| C{Firewall Allow?}
    B -->|Private| D{PE Connected?}
    C -->|No| E[Check Whitelist]
    D -->|No| F[Check DNS/Link]
```

## Sources
- [Configure private endpoints](https://learn.microsoft.com/en-us/azure/storage/common/storage-private-endpoints)
- [Managing storage firewalls](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security)
