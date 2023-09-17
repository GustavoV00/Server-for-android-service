import requests
import json

url = "http://127.0.0.1:8080/windows"  

request_body = {
    "timestamp": "2023-07-10T20:06:42.538",
    "windowStatus": "ACTIVE",
    "windowsNodes": [
        {
            "packageName": "com.android.settings",
            "title": {
                "hasTitle": False,
                "title": "Settings"
            }
        }
    ]
}

for _ in range(100):
    response = requests.post(url, json=request_body)

    if response.status_code == 200:
        print("Request sent successfully")
    else:
        print(f"Request failed with status code: {response.status_code}")