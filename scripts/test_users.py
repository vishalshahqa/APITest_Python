import config.conf
import config.restConf
import util.util
import requests
import pytest


#config alias
sConf = config.conf
sRestconfig = config.restConf
sUtil = util.util
sEnv =  sConf.getEnvDetails("stagging")


@pytest.mark.positiveTest
def test_successfulPostCall():
    #TestSpecific
    data =  open('data/createUser.json')
    sURL = sEnv +'users'
    sPayload = sUtil.jsonReader(data)
    
    print ('url is : ',sURL)
    print ('sPayload is : ',sPayload)
    # rest call.

    sRes = requests.post(sURL,data=sPayload)
    assert sRes.status_code == 201

    #To verify the response.
    sResponseJson = sUtil.textToJson(sRes.text)
    assert sResponseJson['name'] == "morpheus"
    assert sResponseJson['job'] == "leader"

    #Clearing objects
    data.close



@pytest.mark.negativeTest
def test_UnsuccessfulPostCall():
    #TestSpecific
    data =  open('data/createUser.json')
    sURL = sEnv +'users'
    sPayload = sUtil.jsonReader(data)
    
    print ('url is : ',sURL)
    print ('sPayload is : ',sPayload)
    # rest call.

    sRes = requests.post(sURL,data=sPayload)
    assert sRes.status_code == 404

    #To verify the response.
    sResponseJson = sUtil.textToJson(sRes.text)
    assert sResponseJson['name'] == "morpheus"
    assert sResponseJson['job'] == "leader"

    #Clearing objects
    data.close

