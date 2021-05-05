#!/usr/bin/env python

from azure.identity import ClientSecretCredential
from azure.mgmt.network import NetworkManagementClient
from relay_sdk import Interface, Dynamic as D
import logging

logging.basicConfig(level=logging.WARNING)

relay = Interface()

credentials = ClientSecretCredential(
    client_id=relay.get(D.azure.connection.clientID),
    client_secret=relay.get(D.azure.connection.secret),
    tenant_id=relay.get(D.azure.connection.tenantID)
)
subscription_id=relay.get(D.azure.connection.subscriptionID)
network_client = NetworkManagementClient(credentials, subscription_id)


output_list = [] # Output list
resources = [] # List of resources

# If resource group is specified, use that
rg = ''
try:
  rg=relay.get(D.resourceGroup)
except:
  pass

if (rg):
  resources = network_client.network_interfaces.list(rg)

else: 
  resources = network_client.network_interfaces.list_all()

print("Found the following Azure Network Interfaces:\n")
print("{:<30} {:<30} {:<30} {:<100}".format('NAME', 'LOCATION', 'ATTACHED TO', 'ID'))
for r in resources: 
  vm = r.virtual_machine.id.split('/')[8] if r.virtual_machine else ''
  print("{:<30} {:<30} {:<30} {:<100}".format(r.name, r.location, vm, r.id))
  output_list.append(r.as_dict())

print("\nSetting output `networkInterfaces` to list of {} network interfaces".format(len(output_list)))
relay.outputs.set('networkInterfaces', output_list)
