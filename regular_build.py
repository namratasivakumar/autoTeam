import requests
import json

url = "https://tpteamcity.corp.theplatform.com/app/rest/buildQueue"

headers = {
    "Content-Type": "application/json",
"Authorization": "Bearer eyJ0eXAiOiAiVENWMiJ9.bUtSVVJBZmhwZUZBMDVGNS13ejJNTnFkUmJn.OGE1NjM1N2EtOWVlYi00M2VkLTg0MjAtYTgxZjQ1N2VmMTRj"
}
build_id = input("Enter Build ID: ")
response = requests.post(url, headers=headers, data=json.dumps({"buildType": {"id": build_id}}), verify=False)
print(response.text)
if response.status_code == 200:
    print("Build Queued!")
else:
    print("Build Not Queued!")
