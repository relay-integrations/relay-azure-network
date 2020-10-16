# azure-network-step-load-balancer-delete

This [Azure](https://azure.microsoft.com/en-us/services/load-balancer/) step container deletes a set of 
Azure Load Balancers in an Azure subscription given a set of resource IDs

## Notes
To get the Azure Load Balancer resource IDs, try the following command using the Azure CLI: 
 ```
$ az network lb list | jq ".[].id"
"/subscriptions/c82736f2-c108-452b-8178-f548c95d18fe/resourceGroups/rg1/providers/Microsoft.Network/loadBalancers/lb1"
"/subscriptions/c82736f2-c108-452b-8178-f548c95d18fe/resourceGroups/rg2/providers/Microsoft.Network/loadBalancers/lb2"
```

For more information on Resource IDs, check out the [documentation]("https://docs.microsoft.com/en-us/rest/api/resources/resources/getbyid"). 

