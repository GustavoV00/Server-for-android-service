import requests
import json
import random

url = "http://127.0.0.1:8080/windows"  

request_body_1 = {
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
request_body_2 = [
   {
      "timestamp":"2023-10-02T15:22:11.808",
      "windowStatus":"ACTIVE",
      "windowsNodes":[
         {
            "packageName":"com.google.android.apps.nexuslauncher",
            "title":{
               "hasTitle":False,
               "title":"Nexuslauncher"
            }
         }
      ],
      "user":"61333862-6130-3065-6635-666461666137"
   },
   {
      "timestamp":"2023-10-02T15:22:12.015",
      "windowStatus":"SWITCH",
      "windowsNodes":[
         {
            "packageName":"com.google.android.apps.nexuslauncher",
            "title":{
               "hasTitle":False,
               "title":"Nexuslauncher"
            }
         },
         {
            "packageName":"com.google.android.apps.nexuslauncher",
            "title":{
               "hasTitle":True,
               "title":"Settings"
            }
         }
      ],
      "user":"61333862-6130-3065-6635-666461666137"
   },
   {
      "timestamp":"2023-10-02T15:22:12.945",
      "windowStatus":"ACTIVE",
      "windowsNodes":[
         {
            "packageName":"com.android.settings",
            "title":{
               "hasTitle":False,
               "title":"Settings"
            }
         }
      ],
      "user":"61333862-6130-3065-6635-666461666137"
   },
   {
      "timestamp":"2023-10-02T15:22:14.367",
      "windowStatus":"SWITCH",
      "windowsNodes":[
         {
            "packageName":"com.google.android.apps.nexuslauncher",
            "title":{
               "hasTitle":False,
               "title":"Nexuslauncher"
            }
         },
         {
            "packageName":"com.google.android.apps.nexuslauncher",
            "title":{
               "hasTitle":True,
               "title":"Settings"
            }
         }
      ],
      "user":"61333862-6130-3065-6635-666461666137"
   },
   {
      "timestamp":"2023-10-02T15:22:14.865",
      "windowStatus":"ACTIVE",
      "windowsNodes":[
         {
            "packageName":"com.android.settings",
            "title":{
               "hasTitle":False,
               "title":"Settings"
            }
         }
      ],
      "user":"61333862-6130-3065-6635-666461666137"
   }
]

def response_check(response):
    if response.status_code == 200:
        print("Request sent successfully")
    else:
        print(f"Request failed with status code: {response.status_code}")


for _ in range(6000):
    random_number = random.randint(0, 100)
    if (random_number < 50):
        response = requests.post(url, json=request_body_1)
        response_check(response)
    else:
        response = requests.post(url, json=request_body_2)
        response_check(response)
