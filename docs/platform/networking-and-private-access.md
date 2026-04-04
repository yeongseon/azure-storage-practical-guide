# Networking and Private Access

Azure Storage provides multiple networking options to secure and control access to your data from different environments.

| Option | Security | DNS Impact | Cost | Best Use |
| :--- | :--- | :--- | :--- | :--- |
| **Public Access** | Lowest | None | Low | Dev/test only. |
| **Firewall** | Medium | None | Low | Trusted IP ranges. |
| **Service EP** | High | Public IP | Low | VNet-to-Service traffic. |
| **Private EP** | Highest | Private IP | High | Fully isolated access. |

```mermaid
graph TD
    VNet[Azure Virtual Network] -- Private Link --> PE[Private Endpoint]
    PE -- DNS Record --> Storage[Azure Storage Account]
    Internet[Public Internet] -- Restricted IP --> FW[Firewall]
    FW --> Storage
    VNet -- Service Endpoint --> SE[Virtual Network Rules]
    SE --> Storage
```

!!! warning
    Private Endpoints require careful DNS configuration. You must resolve the storage account's FQDN to the private IP address within your virtual network.

## Access Methods
- **Service Endpoints**: Optimizes routing but traffic still reaches the public endpoint.
- **Private Endpoints**: Traffic stays entirely within the Azure backbone, using a private IP.
- **VNet Firewall**: Restricts access to specific subnets or IP addresses.

## Sources
- [Configure Azure Storage firewalls and virtual networks](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security)
- [Use Private Endpoints for Azure Storage](https://learn.microsoft.com/en-us/azure/storage/common/storage-private-endpoints)
