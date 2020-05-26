#!/usr/bin/env python

from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.network import NetworkManagementClient
from nebula_sdk import Interface, Dynamic as D


relay = Interface()

credentials = ServicePrincipalCredentials(
    client_id=relay.get(D.azure.connection.clientID),
    secret=relay.get(D.azure.connection.secret),
    tenant=relay.get(D.azure.connection.tenantID)
)
subscription_id=relay.get(D.azure.connection.subscriptionID)
network_client = NetworkManagementClient(credentials, subscription_id)


output_list = [] # Output list
lbs = [] # List of LBs

# If resource group is specified, use that
rg = ''
try:
  rg=relay.get(D.resourceGroup)
except:
  pass

if (rg):
  lbs = network_client.load_balancers.list(rg)

else: 
  lbs = network_client.load_balancers.list_all()

print("Found the following Azure Load Balancers:\n")
print("{:<30} {:<30} {:<100}".format('NAME', 'LOCATION', 'ID'))
for lb in lbs: 
  print("{:<30} {:<30} {:<100}".format(lb.name, lb.location, lb.id))
  output_list.append(lb.as_dict())

print("\nSetting output `loadBalancers` to list of {} load balancers".format(len(output_list)))
relay.outputs.set('loadBalancers', output_list)