import util.apiTestConf,util.restAPI



reqURL = util.apiTestConf.getEnvDetails("prod")
headerName = util.apiTestConf.getHeader("post") 
payloadName = util.apiTestConf.getPayload("posts")

postRes = util.restAPI.post_API(reqURL,headerName,payloadName)

print(postRes.text)
assert postRes.status_code == 200
assert int(postRes.text["id"]) == 21
