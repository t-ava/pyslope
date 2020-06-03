import requests, json

ENDPOINT = "/ext/keystore"
requestID = 0

# https://docs.ava.network/v1.0/en/api/keystore/



# Create a new user with the specified username and password
# (password should be at least 8 characters 
# and contain upper and lower case letters as well as numbers and symbols)
def createUser(nodeAddr, username, password):
    global requestID
    headers = {'content-type': 'application/json;'}
    requestID = requestID+1
    data = {"jsonrpc":"2.0", "id":requestID, "method" :"keystore.createUser", "params": {"username":username, "password":password}}
    response = requests.post(nodeAddr+ENDPOINT, headers=headers, data=json.dumps(data))
    # print("createUser() response:", response.text)
    # print("success:", response.json()["result"]["success"])
    if "error" in response.json():
        print("API error:", response.json()["error"])
    return response.json()["result"]["success"]



# List the users in this node
def listUsers(nodeAddr):
    global requestID
    headers = {'content-type': 'application/json;'}
    requestID = requestID+1
    data = {"jsonrpc":"2.0", "id":requestID, "method" :"keystore.listUsers"}
    response = requests.post(nodeAddr+ENDPOINT, headers=headers, data=json.dumps(data))
    # print("listUsers() response:", response.text)
    # print("users:", response.json()["result"]["users"])
    if "error" in response.json():
        print("API error:", response.json()["error"])
    return response.json()["result"]["users"]



# Export a user. The user can be imported to another node with keystore.importUser
# The user’s password remains encrypted
def exportUser(nodeAddr, username, password):
    global requestID
    headers = {'content-type': 'application/json;'}
    requestID = requestID+1
    data = {"jsonrpc":"2.0", "id":requestID, "method" :"keystore.exportUser", "params": {"username":username, "password":password}}
    response = requests.post(nodeAddr+ENDPOINT, headers=headers, data=json.dumps(data))
    # print("exportUser() response:", response.text)
    # print("user:", response.json()["result"]["user"])
    if "error" in response.json():
        print("API error:", response.json()["error"])
    return response.json()["result"]["user"]



# Import a user
# @ username: doesn't have to match the username user had when it was exported
# @ password: must match the user's password
# @ user: get this value from exportUser()
def importUser(nodeAddr, username, password, user):
    global requestID
    headers = {'content-type': 'application/json;'}
    requestID = requestID+1
    data = {"jsonrpc":"2.0", "id":requestID, "method" :"keystore.importUser", "params": {"username":username, "password":password}}
    response = requests.post(nodeAddr+ENDPOINT, headers=headers, data=json.dumps(data))
    # print("importUser() response:", response.text)
    # print("success:", response.json()["result"]["success"])
    if "error" in response.json():
        print("API error:", response.json()["error"])
    return response.json()["result"]["success"]
