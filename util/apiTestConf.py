from difflib import Match
import pytest


def getEnvDetails(envName):
    match envName.lower():
        case "prod":
            return "https://fakestoreapi.com/products?title=test product&price=13.5&description=lorem ipsum set&image=https://i.pravatar.cc&category=electronic"        
        case default:
            return print("Sorry!, requested env. details are not available yet")



    
def getHeader(headerName):
    match headerName.lower():
        case "get":
            return {}
        case "post":
            return {"Content-type": "application/json; charset=UTF-8"}
        case default:
            print("Sorry!, It is not supporting requested header yet")

def getPayload(payloadName):
    match payloadName.lower():
        case "posts":
            return {}

        case default:
            return  print("Sorry!, It is not supporting requested payload yet")



# def urlGenerator(envURL,category,restCall):
#     if category == 'products':
#         match restCall:
#             case "POSTS":
#                 return ''+ envURL +'?title='+ title +'price='+price+'description='+description+'&image='+image+'&category='+category
