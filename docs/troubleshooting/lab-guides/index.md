---
description: Troubleshooting lab guides for Azure Storage — reproducible incident labs, expected methodology, and the planned private-endpoint DNS failure starter lab.
---

# Lab Guides

Troubleshooting labs are reproducible experiments that turn a storage symptom into a testable hypothesis, a controlled reproduction, and a falsifiable fix. This hub reserves the Troubleshooting > Lab Guides surface before the first full Azure Storage lab is authored.

## How to Use This Hub

- Start with a symptom-first [playbook](../playbooks/index.md) when you need immediate guidance for a live incident.
- Use a lab guide when you want a controlled environment that reproduces the same failure pattern end to end.
- Expect each future lab to follow the series lab contract: background, hypothesis, runbook, experiment log, evidence, clean-up, and linked playbook context.

## Planned Troubleshooting Labs

| Planned lab | Scenario focus | Current state | Related playbook |
|---|---|---|---|
| Private-endpoint DNS failure | Validate how DNS resolution mistakes break access to a storage account behind a private endpoint | Scaffold only for ZLR-storage-01; full lab content follows in later issues | [Private Endpoint and DNS Issues](../playbooks/access/private-endpoint-and-dns-issues.md) |

## Starter Shape for the First Lab

The first lab candidate will use the canonical troubleshooting-lab structure rather than a prose-only placeholder. When authored, it will include:

1. Lab metadata for difficulty, duration, and scope.
2. `1) Background`, `2) Hypothesis`, `3) Runbook`, and `4) Experiment Log` sections.
3. Evidence sections that capture verification queries and portal or CLI proof.
4. Clean-up guidance plus a cross-link back to the supporting playbook.

## See Also

- [Troubleshooting Home](../index.md)
- [Playbooks](../playbooks/index.md)
- [Private Endpoint and DNS Issues](../playbooks/access/private-endpoint-and-dns-issues.md)
- [First 10 Minutes: Access](../first-10-minutes/access.md)
