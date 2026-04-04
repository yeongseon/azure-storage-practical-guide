# Azure Storage Practical Guide

A practical guide covering Azure Storage data access, durability, operations, and troubleshooting — grounded in MS Learn documentation.

## Scope

- ✅ Included: Storage accounts, Blob, Files, Queue, Table, redundancy, security, networking, lifecycle management
- ❌ Excluded: Azure Data Lake Analytics, Synapse deep dives, Cosmos DB

## Sections

| Section | Purpose |
|---------|---------|
| Start Here | Storage overview, service selection, reading paths |
| Platform | How Azure Storage works — accounts, services, redundancy, access |
| Best Practices | Production-ready storage design and operational guidelines |
| Operations | Step-by-step storage configuration and data management procedures |
| Troubleshooting | Symptom-based storage diagnosis and resolution |
| Reference | Quick-lookup selection guides and cheatsheets |

## Content Source

All content is grounded in official [Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/) documentation.

## Local Build

```bash
pip install mkdocs-material pymdown-extensions
mkdocs build --strict
mkdocs serve
```
