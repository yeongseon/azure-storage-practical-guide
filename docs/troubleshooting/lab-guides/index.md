---
description: Troubleshooting lab guides for Azure Storage — reproducible incident labs, methodology expectations, and the current published and scoped scenarios.
---

# Lab Guides

Troubleshooting labs are reproducible experiments that turn a storage symptom into a testable hypothesis, a controlled reproduction, and a falsifiable fix. This hub introduces the Troubleshooting > Lab Guides surface and tracks both published labs and scoped follow-on scenarios.

## How to Use This Hub

- Start with a symptom-first [playbook](../playbooks/index.md) when you need immediate guidance for a live incident.
- Use a lab guide when you want a controlled environment that reproduces the same failure pattern end to end.
- Expect each future lab to follow the series lab contract: background, hypothesis, runbook, experiment log, evidence, clean-up, and linked playbook context.

## Planned Troubleshooting Labs

| Planned lab | Scenario focus | Current state | Related playbook |
|---|---|---|---|
| [Private-endpoint DNS failure](private-endpoint-dns-failure.md) | Validate how DNS resolution mistakes break access to a storage account behind a private endpoint | First full lab guide published for ZLR-storage-03; live Azure evidence still deferred | [Private Endpoint and DNS Issues](../playbooks/access/private-endpoint-and-dns-issues.md) |
| [Authorization-failure scope](authorization-failure-scope.md) | Plan the second lab that will isolate a Blob data-plane 403 caused by a missing Azure RBAC role such as `Storage Blob Data Reader` | Scoping document published for ZLR-storage-04; full substrate and live evidence still deferred | [Authorization Failures](../playbooks/security/authorization-failures.md) |

## Starter Shape for the First Lab

The first lab guide now documents the canonical troubleshooting-lab structure for the private-endpoint DNS substrate. Use it as the reference shape for future storage troubleshooting labs:

1. Lab metadata for difficulty, duration, and scope.
2. `1) Background`, `2) Hypothesis`, `3) Runbook`, and `4) Experiment Log` sections.
3. Evidence sections that capture verification queries and portal or CLI proof.
4. Clean-up guidance plus a cross-link back to the supporting playbook.

## See Also

- [Troubleshooting Home](../index.md)
- [Playbooks](../playbooks/index.md)
- [Private Endpoint and DNS Issues](../playbooks/access/private-endpoint-and-dns-issues.md)
- [First 10 Minutes: Access](../first-10-minutes/access.md)
