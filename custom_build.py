import requests
import json

url = "https://tpteamcity.corp.theplatform.com/app/rest/buildQueue"

headers = {
    "Content-Type": "application/json",
"Authorization": "Bearer Bearer eyJ0eXAiOiAiVENWMiJ9.bUtSVVJBZmhwZUZBMDVGNS13ejJNTnFkUmJn.OGE1NjM1N2EtOWVlYi00M2VkLTg0MjAtYTgxZjQ1N2VmMTRj"
}
build_id = input("Enter Build ID: ")
branch_name = input("Enter Branch Name: ")
comment = input("Enter Comment: ")
agent = input("Enter Agent ID: ")
isPersonal = True if input("Is Personal Build? (Y/N): ").lower() == "y" else False
property = input("Enter Property Name: ")
value = input("Enter Property Value: ")

payload = {
    "branchName": branch_name,
    "buildType": {
        "id": build_id
    },
    "comment": {
        "text": comment
    },
    "agent": {
        "id": agent
    },
    "properties": {
    "property": [{
              "name": property,
              "value": value
            }
        ]
    },
    "personal": isPersonal
}
response = requests.post(url, headers=headers, data=json.dumps(payload))

if response.status_code == 200:
    print("Custom Build Queued!")
else:
    print("Custom Build Not Queued!")
