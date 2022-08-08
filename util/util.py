import json


def jsonReader(data):
    return json.load(data)

def textToJson(data):
    return json.loads(data)