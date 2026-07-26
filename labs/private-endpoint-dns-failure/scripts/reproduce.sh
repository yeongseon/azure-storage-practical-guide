#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
LAB_DIR="$(cd -- "${SCRIPT_DIR}/.." && pwd)"

RG="${RG:?Set RG to the target resource group name before running this script.}"
LOCATION="${LOCATION:-koreacentral}"
DEPLOYMENT_NAME="${DEPLOYMENT_NAME:-private-endpoint-dns-failure}"
PARAMS_FILE="${PARAMS_FILE:-${LAB_DIR}/parameters.dev.json}"
INJECT_FAULT="${INJECT_FAULT:-true}"
ZONE_NAME="privatelink.blob.core.windows.net"
ZONE_LINK_NAME="${ZONE_LINK_NAME:-blob-zone-link}"

az group create \
    --name "${RG}" \
    --location "${LOCATION}" \
    --output none

az deployment group create \
    --resource-group "${RG}" \
    --name "${DEPLOYMENT_NAME}" \
    --template-file "${LAB_DIR}/main.bicep" \
    --parameters "@${PARAMS_FILE}" \
    --output jsonc

STORAGE_NAME="$(az deployment group show \
    --resource-group "${RG}" \
    --name "${DEPLOYMENT_NAME}" \
    --query properties.outputs.storageAccountName.value \
    --output tsv)"

VM_NAME="$(az deployment group show \
    --resource-group "${RG}" \
    --name "${DEPLOYMENT_NAME}" \
    --query properties.outputs.clientVmName.value \
    --output tsv)"

if [[ "${INJECT_FAULT}" == "true" ]]; then
    az network private-dns link vnet delete \
        --resource-group "${RG}" \
        --zone-name "${ZONE_NAME}" \
        --name "${ZONE_LINK_NAME}" \
        --yes

    printf 'Injected DNS fault by deleting VNet link %s from %s.\n' "${ZONE_LINK_NAME}" "${ZONE_NAME}"
else
    printf 'Deployment completed without fault injection.\n'
fi

printf 'Storage account: %s\n' "${STORAGE_NAME}"
printf 'Client VM: %s\n' "${VM_NAME}"
printf 'Next step: az vm run-command invoke --resource-group %s --name %s --command-id RunShellScript --scripts "nslookup %s.blob.core.windows.net"\n' "${RG}" "${VM_NAME}" "${STORAGE_NAME}"
