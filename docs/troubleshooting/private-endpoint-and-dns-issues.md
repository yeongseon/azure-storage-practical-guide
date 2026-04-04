# Private Endpoint and DNS Issues

Troubleshoot Private Link connectivity and DNS resolution.

| DNS Checklist | Expected Result | Resolution |
|---------------|-----------------|------------|
| nslookup | Private IP (e.g., 10.x.x.x) | Link Private DNS Zone to VNet. |
| DNS Zone Name | `privatelink.blob.core.windows.net` | Create correct zone for service. |
| VNet Link | "Completed" status | Link VNet to Private DNS Zone. |
| Client Resolver | VNet DNS or Forwarder | Configure custom DNS forwarder. |

!!! warning
    The majority of Private Endpoint failures are caused by DNS misconfigurations leading to public IP resolution.

```mermaid
graph TD
    A[Client Request] --> B{Resolve DNS?}
    B -->|Public IP| C[Check VNet Link]
    B -->|Private IP| D{Connect 443?}
    D -->|No| E[Check NSG/Route Table]
    D -->|Yes| F[Access Success]
```

## DNS Validation Checklist

- Confirm service-specific private DNS zone exists.
- Confirm VNet links include every client network.
- Confirm DNS forwarders resolve privatelink zones correctly.
- Confirm endpoint NIC has an expected private IP.
- Confirm NSG and UDR allow required outbound flows.
- Confirm resolution does not intermittently return public IPs.

## See Also

- [Use Private Endpoints](../operations/use-private-endpoints.md)
- [Networking Best Practices](../best-practices/networking-best-practices.md)
- [Cannot Access Storage Account](cannot-access-storage-account.md)

## Sources
- [Troubleshoot Private Endpoint DNS](https://learn.microsoft.com/en-us/azure/private-link/troubleshoot-private-endpoint-connectivity)
- [DNS resolution for storage](https://learn.microsoft.com/en-us/azure/storage/common/storage-private-endpoints?tabs=azure-portal#dns-configuration)
