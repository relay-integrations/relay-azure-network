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


# Getting resource ids & options
resource_ids = None
wait = False 

try:
  resource_ids = relay.get(D.resourceIDs)
except:
  print('No Resource IDs found. Exiting.')
  exit

try:
  wait = relay.get(D.waitForDeletion)
except:
  pass

print('Deleting {} Azure Network Interface(s)'.format(len(resource_ids)))
handle_list = []
for resource_id in resource_ids:
  resource_group_name = resource_id.split('/')[4] # Resource group name
  name = resource_id.split('/')[8] 
  print(resource_id)
  async_operation = network_client.network_interfaces.begin_delete(resource_group_name, name)
  handle_list.append(async_operation)

if wait:
  for op in handle_list:
    print('Waiting for operation to complete')
    op.wait()

print('\nAll specified Network Interfaces are deleted')
