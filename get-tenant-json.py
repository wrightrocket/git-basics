import json
import requests
import pprint
# updated
requests.packages.urllib3.disable_warnings()
encoded_body = json.loads({
    "aaaUser": {
        "attributes": {
            "name": "admin",
            "pwd": "ciscopsdt"
            }
        }
    })
resp = requests.post("https://sandboxapicdc.cisco.com/api/aaaLogin.json", data=encoded_body, verify=False)
header = {"Cookie": "APIC-cookie=" + resp.cookies["APIC-cookie"]}
tenants = requests.get("https://sandboxapicdc.cisco.com/api/node/class/fvTenant.json?rsp-subtree-include=health,faults", headers=header, verify=False)
print(tenants.text)
prettyt = json.loads(tenants.text)
pprint.pp(prettyt)

