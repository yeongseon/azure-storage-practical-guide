targetScope = 'resourceGroup'

@description('Azure region for all regional resources.')
param location string = resourceGroup().location

@description('Short prefix used to derive lab resource names.')
@minLength(3)
@maxLength(11)
param baseName string = 'pednslab'

@description('Globally unique storage account name for the blob private endpoint target.')
@minLength(3)
@maxLength(24)
param storageAccountName string

@description('Linux admin username for the client VM.')
param adminUsername string = 'azureuser'

@description('SSH public key for the client VM administrator account.')
param adminPublicKey string

@description('Azure VM size for the client VM that runs DNS checks.')
param vmSize string = 'Standard_B1s'

@description('Address space for the lab virtual network.')
param vnetAddressPrefix string = '10.42.0.0/16'

@description('Client subnet prefix for the VM that performs DNS checks.')
param clientSubnetPrefix string = '10.42.1.0/24'

@description('Subnet prefix for the storage private endpoint.')
param privateEndpointSubnetPrefix string = '10.42.2.0/24'

var vnetName = '${baseName}-vnet'
var clientSubnetName = 'client-subnet'
var privateEndpointSubnetName = 'private-endpoint-subnet'
var privateDnsZoneName = 'privatelink.blob.${environment().suffixes.storage}'
var zoneLinkName = 'blob-zone-link'
var privateEndpointName = '${baseName}-blob-pe'
var privateEndpointConnectionName = '${baseName}-blob-conn'
var vmNicName = '${baseName}-vmnic'
var vmName = '${baseName}-vm'

resource storageAccount 'Microsoft.Storage/storageAccounts@2023-05-01' = {
  name: storageAccountName
  location: location
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
  properties: {
    accessTier: 'Hot'
    allowBlobPublicAccess: false
    minimumTlsVersion: 'TLS1_2'
    publicNetworkAccess: 'Disabled'
    supportsHttpsTrafficOnly: true
  }
}

resource vnet 'Microsoft.Network/virtualNetworks@2023-09-01' = {
  name: vnetName
  location: location
  properties: {
    addressSpace: {
      addressPrefixes: [
        vnetAddressPrefix
      ]
    }
    subnets: [
      {
        name: clientSubnetName
        properties: {
          addressPrefix: clientSubnetPrefix
        }
      }
      {
        name: privateEndpointSubnetName
        properties: {
          addressPrefix: privateEndpointSubnetPrefix
          privateEndpointNetworkPolicies: 'Disabled'
        }
      }
    ]
  }
}

resource privateDnsZone 'Microsoft.Network/privateDnsZones@2020-06-01' = {
  name: privateDnsZoneName
  location: 'global'
}

resource privateDnsZoneLink 'Microsoft.Network/privateDnsZones/virtualNetworkLinks@2020-06-01' = {
  parent: privateDnsZone
  name: zoneLinkName
  location: 'global'
  properties: {
    registrationEnabled: false
    virtualNetwork: {
      id: vnet.id
    }
  }
}

resource privateEndpoint 'Microsoft.Network/privateEndpoints@2023-09-01' = {
  name: privateEndpointName
  location: location
  properties: {
    subnet: {
      id: resourceId('Microsoft.Network/virtualNetworks/subnets', vnet.name, privateEndpointSubnetName)
    }
    privateLinkServiceConnections: [
      {
        name: privateEndpointConnectionName
        properties: {
          privateLinkServiceId: storageAccount.id
          groupIds: [
            'blob'
          ]
        }
      }
    ]
  }
}

resource privateEndpointDnsZoneGroup 'Microsoft.Network/privateEndpoints/privateDnsZoneGroups@2023-09-01' = {
  parent: privateEndpoint
  name: 'default'
  properties: {
    privateDnsZoneConfigs: [
      {
        name: 'blob-zone-config'
        properties: {
          privateDnsZoneId: privateDnsZone.id
        }
      }
    ]
  }
  dependsOn: [
    privateDnsZoneLink
  ]
}

resource vmNic 'Microsoft.Network/networkInterfaces@2023-09-01' = {
  name: vmNicName
  location: location
  properties: {
    ipConfigurations: [
      {
        name: 'ipconfig1'
        properties: {
          privateIPAllocationMethod: 'Dynamic'
          subnet: {
            id: resourceId('Microsoft.Network/virtualNetworks/subnets', vnet.name, clientSubnetName)
          }
        }
      }
    ]
  }
}

resource clientVm 'Microsoft.Compute/virtualMachines@2024-03-01' = {
  name: vmName
  location: location
  properties: {
    hardwareProfile: {
      vmSize: vmSize
    }
    osProfile: {
      computerName: vmName
      adminUsername: adminUsername
      linuxConfiguration: {
        disablePasswordAuthentication: true
        ssh: {
          publicKeys: [
            {
              path: '/home/${adminUsername}/.ssh/authorized_keys'
              keyData: adminPublicKey
            }
          ]
        }
      }
    }
    storageProfile: {
      imageReference: {
        publisher: 'Canonical'
        offer: '0001-com-ubuntu-server-jammy'
        sku: '22_04-lts-gen2'
        version: 'latest'
      }
      osDisk: {
        createOption: 'FromImage'
        managedDisk: {
          storageAccountType: 'Standard_LRS'
        }
      }
    }
    networkProfile: {
      networkInterfaces: [
        {
          id: vmNic.id
        }
      ]
    }
  }
}

resource clientVmBootstrap 'Microsoft.Compute/virtualMachines/extensions@2024-03-01' = {
  parent: clientVm
  name: 'install-dnsutils'
  location: location
  properties: {
    publisher: 'Microsoft.Azure.Extensions'
    type: 'CustomScript'
    typeHandlerVersion: '2.1'
    autoUpgradeMinorVersion: true
    settings: {
      commandToExecute: 'bash -c "apt-get update && apt-get install -y dnsutils curl"'
    }
  }
}

output storageAccountName string = storageAccount.name
output storageBlobFqdn string = '${storageAccount.name}.blob.${environment().suffixes.storage}'
output privateEndpointName string = privateEndpoint.name
output privateDnsZoneName string = privateDnsZone.name
output privateDnsZoneLinkName string = zoneLinkName
output clientVmName string = clientVm.name
output clientVnetName string = vnet.name
