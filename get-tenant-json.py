import json
import requests

requests.packages.urllib3.disable_warnings()
encoded_body = json.dumps({
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

