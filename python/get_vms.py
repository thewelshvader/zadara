import requests
import json
import getpass
token = ""
# token = getpass.getpass(prompt='Token: ', stream=None) 
headers = {
           'X-Auth-Token': token
           }
def get_vm_list():
    url = "https://compute-cyxtera-10.zadara.com/api-explorer/api/v2/compute/vms"
    response = requests.get(url, headers=headers)
    return response.json()
    
for vm in get_vm_list():
    print(vm['name'])



