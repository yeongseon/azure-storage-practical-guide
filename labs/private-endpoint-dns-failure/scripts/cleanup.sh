#!/usr/bin/env bash
set -euo pipefail

RG="${RG:?Set RG to the target resource group name before running cleanup.}"

az group delete \
    --name "${RG}" \
    --yes \
    --no-wait
