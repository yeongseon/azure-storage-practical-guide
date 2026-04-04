# Data Protection and Recovery Issues

Recover from accidental data deletion or corruption.

| Protection Feature | Recovery Capability | Recovery Tool |
|--------------------|---------------------|---------------|
| Soft Delete | Restore deleted objects. | Portal/PowerShell |
| Versioning | Rollback to previous state. | Portal/SDK |
| Backup | Point-in-time recovery. | Backup Center |
| Snapshot | Manual point-in-time state. | Storage Explorer |

!!! note
    Always verify which data protection features were enabled BEFORE the incident occurred.

```mermaid
graph TD
    A[Data Lost] --> B{Soft Delete On?}
    B -->|Yes| C[Undelete]
    B -->|No| D{Versioning On?}
    D -->|Yes| E[Restore Version]
    D -->|No| F[Check Backup]
```

## Sources
- [Recovering deleted blobs](https://learn.microsoft.com/en-us/azure/storage/blobs/soft-delete-blob-overview#restoring-soft-deleted-blobs)
- [Backup and recovery for storage](https://learn.microsoft.com/en-us/azure/backup/azure-backup-storage-introduction)
