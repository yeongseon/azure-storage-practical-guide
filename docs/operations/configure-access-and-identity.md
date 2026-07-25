---
content_sources:
  diagrams:
    - id: operations-configure-access-and-identity
      type: flowchart
      source: mslearn-adapted
      mslearn_url: https://learn.microsoft.com/en-us/azure/storage/common/storage-auth
content_validation:
  status: pending_review
  last_reviewed: '2026-07-25'
  reviewer: agent
  core_claims:
    - claim: Azure Storage supports Microsoft Entra authorization, Shared Key, and SAS-based access patterns.
      source: https://learn.microsoft.com/en-us/azure/storage/common/storage-auth
      verified: false
    - claim: Azure RBAC data roles control data-plane access to storage resources.
      source: https://learn.microsoft.com/en-us/azure/storage/blobs/assign-azure-role-data-access
      verified: false
---

# Configure Access and Identity

Secure storage access using RBAC and identity-based controls.

| RBAC Role | Permissions | Use Case |
|-----------|-------------|----------|
| Storage Blob Data Reader | Read-only access to blobs. | Application read operations. |
| Storage Blob Data Contributor | Read/write/delete blobs. | Application data management. |
| Storage Blob Data Owner | Full access to blob containers and data; can set POSIX ACLs for HNS-enabled accounts. Does not grant RBAC role assignment. | Data ownership / ACL management. |
| Storage Account Contributor | Manage account settings. | Infrastructure management. |

!!! warning
    Disable shared key access whenever possible to enforce modern identity-based authentication.

<!-- diagram-id: operations-configure-access-and-identity -->
```mermaid
graph TD
    A[Identify Identity] --> B[Assign RBAC Role]
    B --> C[Set Scope: Account/Container]
    C --> D[Test Access]
    D --> E[Monitor Access Logs]
```

## Access Validation Checklist

- Verify principal type: user, group, or managed identity.
- Assign data plane roles for data operations.
- Assign control plane roles only for resource management.
- Scope assignments to subscription, account, container, or share.
- Validate token audience and tenant alignment.
- Confirm diagnostics capture authorization failures.

## See Also

- [Access Models](../platform/access-models.md)
- [Security Best Practices](../best-practices/security-best-practices.md)
- [Authorization Failures](../troubleshooting/playbooks/security/authorization-failures.md)

## Sources
- [Authorize access to storage](https://learn.microsoft.com/en-us/azure/storage/common/storage-auth)
- [Assign Azure roles for access](https://learn.microsoft.com/en-us/azure/storage/blobs/assign-azure-role-data-access)
