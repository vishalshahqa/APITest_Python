import json
import requests
import json

def post_API(reqURL,headerName,payloadName):
    payload = json.dumps(payloadName)
    postRes = requests.request("POST",reqURL,headers=headerName, data=payload)
    return postRes
    

def get_call(reqURL,expStatusCode):
    payload={}
    headers = {}

    getRes = requests.request("GET",reqURL,headers=headers, data=payload)
    print(getRes.text)

    assert getRes.status_code == expStatusCode

def patch_call():
    pass

def delete_call():
    pass
   