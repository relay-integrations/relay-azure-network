# azure-network-step-nic-delete

This [Azure](https://azure.microsoft.com/en-us/services/#networking) step container deletes a set of 
Azure Network Interfaces in an Azure subscription given a set of resource IDs


## Notes
To get the Azure Load Balancer resource IDs, try the following command using the Azure CLI: 
 ```
$ az network nic list | jq ".[].id"
"/subscriptions/c82736f2-c108-452b-8178-f548c95d18fe/resourceGroups/rg1/providers/Microsoft.Network/networkInterfaces/nic1"
```

For more information on Resource IDs, check out the [documentation]("https://docs.microsoft.com/en-us/rest/api/resources/resources/getbyid"). 

