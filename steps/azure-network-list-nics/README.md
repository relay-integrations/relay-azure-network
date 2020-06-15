# azure-network-list-network-interfaces

This [Azure](hhttps://azure.microsoft.com/en-us/services/#networking/) step container lists the network interfaces
in an Azure subscription or resource group and sets an output, `networkInterfaces`, to an array of network interface objects.

## Specification

| Setting | Child setting | Data type | Description | Default | Required |
|---------|---------------|-----------|-------------|---------|----------|
| `azure` || mapping | A mapping of Azure account configuration. | None | True |
|| `connection` | Azure Connection | Connection for the Azure account. Use the Connection sidebar to configure the Azure Connection | None | True |
| `resourceGroup` || string | Resource group to look under | None | False | 

## Outputs

| Name | Data type | Description |
|------|-----------|-------------|
| `networkInterfaces` | array of Azure Network Interfaces | List of Azure Network Interfaces and metadata. |

## Example

```yaml
steps:
# ...
- name: list-nics
  image: projectnebula/azure-network-list-nics
  spec:
    azure:
      connection: !Connection { type: azure, name: my-azure-account }
    resourceGroup: 'my_resource_group' 
```

## Example output `networkInterfaces`

```
[
   {
      "id":"/subscriptions/c82736f2-c108-452b-8178-f548c95d18fe/resourceGroups/rg1/providers/Microsoft.Network/networkInterfaces/nic1",
      "name":"nic-1",
      "type":"Microsoft.Network/networkInterfaces",
      "location":"westus",
      "virtual_machine":{
         "id":"/subscriptions/c82736f2-c108-452b-8178-f548c95d18fe/resourceGroups/rg1/providers/Microsoft.Compute/virtualMachines/vm1"
      },
      "network_security_group":{
         "id":"/subscriptions/c82736f2-c108-452b-8178-f548c95d18fe/resourceGroups/rg1/providers/Microsoft.Network/networkSecurityGroups/vm1-nsg"
      },
      "ip_configurations":[
         {
            "id":"/subscriptions/c82736f2-c108-452b-8178-f548c95d18fe/resourceGroups/rg1/providers/Microsoft.Network/networkInterfaces/vm1654/ipConfigurations/ipconfig1",
            "private_ip_address":"192.168.1.4",
            "private_ip_allocation_method":"Dynamic",
            "private_ip_address_version":"IPv4",
            "subnet":{
               "id":"/subscriptions/c82736f2-c108-452b-8178-f548c95d18fe/resourceGroups/rg1/providers/Microsoft.Network/virtualNetworks/puppet-remediate-vnet/subnets/default"
            },
            "primary":True,
            "public_ip_address":{
               "id":"/subscriptions/c82736f2-c108-452b-8178-f548c95d18fe/resourceGroups/rg1/providers/Microsoft.Network/publicIPAddresses/vm1-ip"
            },
            "provisioning_state":"Succeeded",
            "name":"ipconfig1",
            "etag":"W/\"d53dd7cc-0c6c-4ebb-af6e-ac29e8036936\""
         }
      ],
      "tap_configurations":[

      ],
      "dns_settings":{
         "dns_servers":[

         ],
         "applied_dns_servers":[

         ]
      },
      "mac_address":"00-0D-3A-5C-18-D0",
      "primary":True,
      "enable_accelerated_networking":False,
      "enable_ip_forwarding":False,
      "hosted_workloads":[

      ],
      "resource_guid":"c0ce4e94-76dd-4d5e-9449-3315de640fd5",
      "provisioning_state":"Succeeded",
      "etag":"W/\"d53dd7cc-0c6c-4ebb-af6e-ac29e8036936\""
   }
   ...
]
```

