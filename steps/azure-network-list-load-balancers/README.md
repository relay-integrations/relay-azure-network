# azure-network-list-load-balancers

This [Azure](https://azure.microsoft.com/en-us/services/load-balancer/) step container lists the load 
balancers in an Azure subscription or resource group and sets an output, `loadbalancers`, to an array of 
load balancer objects.

## Specification

| Setting | Child setting | Data type | Description | Default | Required |
|---------|---------------|-----------|-------------|---------|----------|
| `azure` || mapping | A mapping of Azure account configuration. | None | True |
|| `connection` | Azure Connection | Connection for the Azure account. Use the Connection sidebar to configure the Azure Connection | None | True |
| `resourceGroup` || string | Resource group to look under | None | False | 

## Outputs

| Name | Data type | Description |
|------|-----------|-------------|
| `loadbalancers` | array of Azure Load Balancers | List of Azure Load Balancers and metadata. |

## Example

```yaml
steps:
# ...
- name: list-load-balancers
  image: projectnebula/azure-network-list-load-balancers
  spec:
    azure:
      connection: !Connection { type: azure, name: my-azure-account }
    resourceGroup: 'my_resource_group' 
```

## Example output `loadBalancers`

```
[
   {
      "id":"/subscriptions/c82736fq-c108-452b-8178-f548c95d18fe/resourceGroups/rg1/providers/Microsoft.Network/loadBalancers/lb-1",
      "name":"lb-1",
      "type":"Microsoft.Network/loadBalancers",
      "location":"westus2",
      "tags":{

      },
      "sku":{
         "name":"Basic"
      },
      "frontend_ip_configurations":[
         {
            "id":"/subscriptions/c82736fq-c108-452b-8178-f548c95d18fe/resourceGroups/rg1/providers/Microsoft.Network/loadBalancers/lb-1/frontendIPConfigurations/LoadBalancerFrontEnd",
            "private_ip_allocation_method":"Dynamic",
            "private_ip_address_version":"IPv4",
            "public_ip_address":{
               "id":"/subscriptions/c82736fq-c108-452b-8178-f548c95d18fe/resourceGroups/rg1/providers/Microsoft.Network/publicIPAddresses/ip-1"
            },
            "provisioning_state":"Succeeded",
            "name":"LoadBalancerFrontEnd",
            "etag":"W/\"3abe3cd4-8c21-46bf-9bd5-ecae3766c5f8\"",
            "type":"Microsoft.Network/loadBalancers/frontendIPConfigurations"
         }
      ],
      "backend_address_pools":[

      ],
      "load_balancing_rules":[

      ],
      "probes":[

      ],
      "inbound_nat_rules":[

      ],
      "inbound_nat_pools":[

      ],
      "resource_guid":"c98b62e9-991e-483a-a87d-8e934105eb08",
      "provisioning_state":"Succeeded",
      "etag":"W/\"3abe3cd4-8c21-46bf-9bd5-ecae3766c5f8\""
   }
]
```

