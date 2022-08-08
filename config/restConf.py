  
def getHeader(headerName):
    match headerName.lower():
        case "get":
            return {}
        case "post":
            return {"Content-type": "application/json; charset=UTF-8"}
        case default:
            print("Sorry!, It is not supporting requested header yet")

