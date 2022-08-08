import config.conf
import config.restConf
import util.util
import data
import requests


#config alias
sConf = config.conf
sRestconfig = config.restConf
sUtil = util.util
data =  open('data/userCreation.json')

#TestSpecific
sEnv =  sConf.getEnvDetails("stagging") + 'users'
sPayload = sUtil.jsonReader(data)
sHeader = sRestconfig.getHeader("post")

# rest call.

sRes = requests.post(sEnv,data=sPayload)
assert sRes.status_code == 201

#To verify the response.
sResponseJson = sUtil.textToJson(sRes.text)
assert sResponseJson['name'] == "morpheus"
assert sResponseJson['job'] == "leader"

#Clearing objects
data.close
