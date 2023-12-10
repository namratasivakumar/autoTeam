from typing import Union
from fastapi import FastAPI
import requests
import json

app = FastAPI()

@app.post("/")
def readCommand():
    url = "https://tpteamcity.corp.theplatform.com/app/rest/buildQueue"

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer eyJ0eXAiOiAiVENWMiJ9.bUtSVVJBZmhwZUZBMDVGNS13ejJNTnFkUmJn.OGE1NjM1N2EtOWVlYi00M2VkLTg0MjAtYTgxZjQ1N2VmMTRj"
    }
    build_id = "ProductDev_Rmp_CmpServices_UploadSimulator"
    response = requests.post(url, headers=headers, data=json.dumps({"buildType": {"id": build_id}}), verify=False)
    print(response.text)
    if response.status_code == 200:
        return {"Hello": "World"}