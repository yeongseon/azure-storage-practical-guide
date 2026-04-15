# Azure Storage Practical Guide

[English](README.md) | [한국어](README.ko.md) | [日本語](README.ja.md) | [简体中文](README.zh-CN.md)

A practical guide covering Azure Storage data access, durability, operations, and troubleshooting — grounded in MS Learn documentation.

## What's Inside

| Section | Description |
|---------|-------------|
| [Start Here](https://yeongseon.github.io/azure-storage-practical-guide/start-here/) | Storage overview, service selection guide, and common usage scenarios |
| [Platform](https://yeongseon.github.io/azure-storage-practical-guide/platform/) | Deep dive into accounts, Blob, File, Queue, and Table services with redundancy models |
| [Best Practices](https://yeongseon.github.io/azure-storage-practical-guide/best-practices/) | Production-ready design for security, networking, performance, and lifecycle management |
| [Operations](https://yeongseon.github.io/azure-storage-practical-guide/operations/) | Day-2 guide for managing containers, shares, private endpoints, and data movement |
| [Tutorials](https://yeongseon.github.io/azure-storage-practical-guide/tutorials/) | Hands-on labs for lifecycle policies, AD integration, and static websites with CDN |
| [Troubleshooting](https://yeongseon.github.io/azure-storage-practical-guide/troubleshooting/) | Diagnosis playbooks for access denied, throttling, and replication lag issues |
| [Reference](https://yeongseon.github.io/azure-storage-practical-guide/reference/) | Quick-lookup for service selection, redundancy options, and access cheatsheets |

## Storage Services

Detailed coverage of Azure Storage offerings:
- **Blob Storage**: Scalable object storage for unstructured data and static websites
- **Azure Files**: Managed file shares with AD integration and SMB/NFS support
- **Queue Storage**: Messaging store for workflow processing and communication
- **Table Storage**: NoSQL key-attribute store for rapid development
- **Redundancy**: Implementation of LRS, ZRS, GRS, and GZRS for data durability

## Quick Start

```bash
# Clone the repository
git clone https://github.com/yeongseon/azure-storage-practical-guide.git

# Install MkDocs dependencies
pip install mkdocs-material mkdocs-minify-plugin

# Start local documentation server
mkdocs serve
```

Visit `http://127.0.0.1:8000` to browse the documentation locally.

## Contributing

Contributions welcome! Please see our [Contributing Guide](https://yeongseon.github.io/azure-storage-practical-guide/contributing/) for:

- Repository structure and content organization
- Document templates and writing standards
- Local development setup and build validation
- Pull request process

## Related Projects

| Repository | Description |
|---|---|
| [azure-virtual-machine-practical-guide](https://github.com/yeongseon/azure-virtual-machine-practical-guide) | Azure Virtual Machines practical guide |
| [azure-networking-practical-guide](https://github.com/yeongseon/azure-networking-practical-guide) | Azure Networking practical guide |
| [azure-app-service-practical-guide](https://github.com/yeongseon/azure-app-service-practical-guide) | Azure App Service practical guide |
| [azure-functions-practical-guide](https://github.com/yeongseon/azure-functions-practical-guide) | Azure Functions practical guide |
| [azure-container-apps-practical-guide](https://github.com/yeongseon/azure-container-apps-practical-guide) | Azure Container Apps practical guide |
| [azure-communication-services-practical-guide](https://github.com/yeongseon/azure-communication-services-practical-guide) | Azure Communication Services practical guide |
| [azure-kubernetes-service-practical-guide](https://github.com/yeongseon/azure-kubernetes-service-practical-guide) | Azure Kubernetes Service (AKS) practical guide |
| [azure-architecture-practical-guide](https://github.com/yeongseon/azure-architecture-practical-guide) | Azure Architecture practical guide |
| [azure-monitoring-practical-guide](https://github.com/yeongseon/azure-monitoring-practical-guide) | Azure Monitoring practical guide |

## Disclaimer

This is an independent community project. Not affiliated with or endorsed by Microsoft. Azure and Azure Storage are trademarks of Microsoft Corporation.

## License

[MIT](LICENSE)

