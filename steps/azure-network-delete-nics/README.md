# azure-network-delete-network-interfaces

This [Azure](https://azure.microsoft.com/en-us/services/#networking) step container deletes a set of 
Azure Network Interfaces in an Azure subscription given a set of resource IDs

## Specification

| Setting | Child setting | Data type | Description | Default | Required |
|---------|---------------|-----------|-------------|---------|----------|
| `azure` || mapping | A mapping of Azure account configuration. | None | True |
|| `connection` | Azure Connection | Connection for the Azure account. Use the Connection sidebar to configure the Azure Connection | None | True |
| `resourceIDs` ||  An array of resource IDs | The list of resource IDs to be deleted | None | True |
| `waitForDeletion` ||  boolean | Determines whether to wait for deletion before continuing | False | False | 


## Outputs
None

## Example

```yaml
steps:
# ...
- name: delete-nics
  image: projectnebula/azure-network-delete-network-interfaces
  spec:
    azure:
      connection: !Connection { type: azure, name: my-azure-account }
    waitForDeletion: true
    resourceIDs:
    - /subscriptions/c82736f2-c108-452b-8178-f548c95d18fe/resourceGroups/rg1/providers/Microsoft.Network/networkInterfaces/nic1
 
```

## Notes
To get the Azure Load Balancer resource IDs, try the following command using the Azure CLI: 
 ```
$ az network nic list | jq ".[].id"
"/subscriptions/c82736f2-c108-452b-8178-f548c95d18fe/resourceGroups/rg1/providers/Microsoft.Network/networkInterfaces/nic1"
```

For more information on Resource IDs, check out the [documentation]("https://docs.microsoft.com/en-us/rest/api/resources/resources/getbyid"). 

