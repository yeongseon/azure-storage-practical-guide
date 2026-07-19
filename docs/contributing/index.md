# Contributing

Thank you for your interest in contributing to Azure Storage Practical Guide!

## Quick Start

1. Fork the repository
2. Clone: `git clone https://github.com/yeongseon/azure-storage-practical-guide.git`
3. Install dependencies: `pip install mkdocs-material mkdocs-minify-plugin`
4. Start local preview: `mkdocs serve`
5. Open `http://127.0.0.1:8000` in your browser
6. Create a feature branch: `git checkout -b feature/your-change`
7. Make changes and validate: `mkdocs build --strict`
8. Submit a Pull Request

## Repository Structure

```text
.
├── .github/
│   └── workflows/              # GitHub Pages deployment
├── docs/
│   ├── assets/                 # Images, icons
│   ├── best-practices/         # Production patterns and anti-patterns
│   ├── javascripts/            # Mermaid zoom JS
│   ├── operations/             # Day-2 operational execution
│   ├── platform/               # Architecture and design decisions
│   ├── reference/              # CLI cheatsheet, decision guides
│   ├── start-here/             # Overview, learning paths
│   ├── stylesheets/            # Custom CSS
│   └── troubleshooting/        # Diagnosis and resolution
└── mkdocs.yml                  # MkDocs Material configuration
```

## Content Categories

| Section | Purpose |
|---|---|
| **Start Here** | Entry points, learning paths, overview |
| **Platform** | Architecture, design decisions — WHAT and HOW it works |
| **Best Practices** | Production patterns — HOW to use the platform well |
| **Operations** | Day-2 execution — HOW to run in production |
| **Troubleshooting** | Diagnosis and resolution |
| **Reference** | Quick lookup — CLI, decision guides |

## Document Templates

Every document must follow the template for its section.

### Platform docs

```text
# Title
Brief introduction (1-2 sentences)
## Main Content
### Subsections
## See Also
## Sources
```

### Best Practices docs

```text
# Title
Brief introduction
## Why This Matters
## Recommended Practices
## Common Mistakes / Anti-Patterns
## Validation Checklist
## See Also
## Sources
```

### Operations docs

```text
# Title
Brief introduction
## Prerequisites
## When to Use
## Procedure
## Verification
## Rollback / Troubleshooting
## See Also
## Sources
```

### Troubleshooting docs

```text
# Title
## Symptom
## Possible Causes
## Diagnosis Steps
## Resolution
## Prevention
## See Also
## Sources
```

### Reference docs

```text
# Title
Brief introduction
## Topic/Command Groups
## Usage Notes
## See Also
## Sources
```

## Writing Standards

### CLI Commands
```bash
# ALWAYS use long flags for readability
az storage account create --resource-group $RG --name $STORAGE_NAME --location $LOCATION

# NEVER use short flags in documentation
az storage account create -g $RG -n $STORAGE_NAME  # ❌ Don't do this
```

| Command | Purpose |
| --- | --- |
| `az storage account create` | Create a storage account (shown with readable long flags). |
| `--resource-group` | Resource group that will contain the account. |
| `--name` | Globally unique name of the storage account. |
| `--location` | Azure region for the account. |
| `az storage account create -g $RG -n $STORAGE_NAME  # ❌ Don't do this` |  |


### Variables
| Variable | Description | Example |
|----------|-------------|---------|
| `$RG` | Resource group name | `rg-storage-demo` |
| `$STORAGE_NAME` | Storage account name | `stdemostorage001` |
| `$CONTAINER_NAME` | Blob container name | `documents` |
| `$SHARE_NAME` | File share name | `fileshare-001` |
| `$LOCATION` | Azure region | `koreacentral` |
| `$SUBSCRIPTION_ID` | Subscription identifier placeholder | `<subscription-id>` |

### Mermaid Diagrams
All architectural diagrams use Mermaid. Every page should include at least one diagram.

### Nested Lists
4-space indent required.

### Admonitions
4-space indent for body content.

### Tail Sections
1. `## See Also` — internal cross-links
2. `## Sources` — Microsoft Learn URLs

## Content Source Policy
All content MUST be traceable to official Microsoft Learn documentation.

| Type | Description | Allowed? |
|---|---|---|
| `mslearn` | Directly from Microsoft Learn | Required for platform content |
| `mslearn-adapted` | Microsoft Learn content adapted for this guide | Allowed with source URL |
| `self-generated` | Original content for this guide | Requires justification |
| `community` | From community sources | Not for core content |
| `unknown` | Source not documented | Must be validated |

## PII Rules
**CRITICAL**: All CLI output examples MUST have PII removed.

**Must mask (real Azure identifiers):**

- Subscription IDs: `<subscription-id>`
- Tenant IDs: `<tenant-id>`
- Object IDs: `<object-id>`
- Resource IDs containing real subscription/tenant
- Emails: Remove or mask as `user@example.com`
- Storage keys: NEVER include
- SAS tokens: NEVER include
- Connection strings: `<connection-string>`

## Build and Validate
```bash
pip install mkdocs-material mkdocs-minify-plugin
mkdocs build --strict
mkdocs serve
```

## Git Commit Style
`type: short description` — types: feat, fix, docs, chore, refactor

## Review Process
1. CI checks (MkDocs build)
2. Maintainer review
3. Merge triggers deployment

## Code of Conduct
See [CODE_OF_CONDUCT.md](https://github.com/yeongseon/azure-storage-practical-guide/blob/main/CODE_OF_CONDUCT.md).

## See Also
- [Repository Map](../start-here/index.md)
