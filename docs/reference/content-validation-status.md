---
content_sources:
  diagrams:
    - id: reference-content-validation-status
      type: pie
      source: self-generated
      justification: "Repository content-source summary generated from local documentation metadata."
      based_on:
        - https://learn.microsoft.com/en-us/azure/storage/
    - id: reference-content-validation-status-2
      type: flowchart
      source: self-generated
      justification: "Repository content-source summary generated from local documentation metadata."
      based_on:
        - https://learn.microsoft.com/en-us/azure/storage/
---

# Content Source Validation Status

This page tracks the source validation status of documentation content, including diagrams and text. All content must be traceable to official Microsoft Learn documentation.

## Summary

*Generated: 2026-04-10*

| Content Type | Total | MS Learn Sourced | Self-Generated | No Source |
|---|---:|---:|---:|---:|
| Mermaid Diagrams | 91 | 88 | 3 | 0 |
| Text Sections | — | — | — | — |

!!! warning "Validation Required"
    All 91 mermaid diagrams now include source metadata. Repository-only dashboards remain self-generated with justification:
    
    1. 88 diagrams are marked as `mslearn-adapted` with official Microsoft Learn URLs.
    2. 3 repository-status diagrams are marked as `self-generated` with justification.

<!-- diagram-id: reference-content-validation-status -->
```mermaid
pie title Content Source Status
    "MS Learn Adapted" : 88
    "Self-Generated" : 3
```

## Validation Categories

### Source Types

| Type | Description | Allowed? |
|---|---|---|
| `mslearn` | Content directly from Microsoft Learn | Yes |
| `mslearn-adapted` | Microsoft Learn content adapted for this guide | Yes, with source URL |
| `self-generated` | Original content created for this guide | Requires justification |
| `community` | From community sources | Not for core content |
| `unknown` | Source not documented | Must be validated |

### Diagram Validation Status

All mermaid diagrams now include source metadata and diagram IDs. Review fidelity again when upstream Microsoft Learn guidance changes.

## How to Validate Content

### Step 1: Add Source Metadata to Frontmatter

Add `content_sources` to the document's YAML frontmatter:

```yaml
---
title: Example Page
content_sources:
  diagrams:
    - id: architecture-overview
      type: flowchart
      source: mslearn
      mslearn_url: https://learn.microsoft.com/en-us/azure/storage/
    - id: request-flow
      type: sequence
      source: self-generated
      justification: "Synthesized from multiple Microsoft Learn articles for clarity"
      based_on:
        - https://learn.microsoft.com/en-us/azure/storage/
  text:
    - section: "## Summary"
      source: mslearn-adapted
      mslearn_url: https://learn.microsoft.com/en-us/azure/storage/
---
```

### Step 2: Mark Diagram Blocks with IDs

Add an HTML comment before each mermaid block to identify it:

```markdown
<!-- diagram-id: reference-content-validation-status-2 -->
```mermaid
flowchart TD
    A[Client] --> B[Azure Storage]
```
```

### Step 3: Run Validation Script

```bash
python3 scripts/validate_content_sources.py
```

### Step 4: Update This Page

```bash
python3 scripts/generate_content_validation_status.py
```

## Validation Rules

!!! danger "Mandatory Rules"
    1. Platform diagrams (`docs/platform/`) must have Microsoft Learn sources
    2. Architecture diagrams must reference official Microsoft documentation
    3. Troubleshooting flowcharts may be self-generated if they synthesize Microsoft Learn content
    4. Self-generated content must have a `justification` field explaining the source basis

## See Also

- [Validation Status](validation-status.md)
- [Reference Index](index.md)

## Sources

- [Microsoft Learn: Azure Storage documentation](https://learn.microsoft.com/en-us/azure/storage/)
