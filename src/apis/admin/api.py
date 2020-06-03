import requests, json

ENDPOINT = "/ext/admin"
requestID = 0

# https://docs.ava.network/v1.0/en/api/admin/



# Example: how to use these APIs -> try & except
# try:
#     print(alias('http://127.0.0.1:9650', "bc/x", "myAlias"))
# except Exception as e:
#     print("API failed:", e)



# Get the peers this node is connected to
# @ nodeAddr: node's ip address (ex. 'http://127.0.0.1:9650')
def peers(nodeAddr):
    global requestID
    headers = {'content-type': 'application/json;'}
    requestID = requestID+1
    data = {"jsonrpc":"2.0", "id":requestID, "method" :"admin.peers"}               
    response = requests.post(nodeAddr+ENDPOINT, headers=headers, data=json.dumps(data))
    # print("peers() response:", response.text)
    # print("peers:", response.json()["result"]["peers"])
    if "error" in response.json():
        print("API error:", response.json()["error"])
    return response.json()["result"]["peers"]



# Get the ID of the network this node is participating in
def getNetworkID(nodeAddr):
    global requestID
    headers = {'content-type': 'application/json;'}
    requestID = requestID+1
    data = {"jsonrpc":"2.0", "id":requestID, "method" :"admin.getNetworkID"}
    response = requests.post(nodeAddr+ENDPOINT, headers=headers, data=json.dumps(data))
    # print("getNetworkID() response:", response.text)
    # print("networkID:", response.json()["result"]["networkID"])
    if "error" in response.json():
        print("API error:", response.json()["error"])
    return response.json()["result"]["networkID"]



# Assign an API an alias, a different endpoint for the API
# The original endpoint will still work
# This change only affects this node. other nodes will not know about this alias.
# @ endpoint: the original endpoint of the API. endpoint should only include the part of the endpoint after /ext/
#             (ex. "bc/x")
# @ alias: The API being aliased can now be called at ext/alias (ex. "myAlias")
def alias(nodeAddr, endpoint, alias):
    global requestID
    headers = {'content-type': 'application/json;'}
    requestID = requestID+1
    data = {"jsonrpc":"2.0", "id":requestID, "method" :"admin.alias", "params": {"alias":alias, "endpoint":endpoint}}
    response = requests.post(nodeAddr+ENDPOINT, headers=headers, data=json.dumps(data))
    # print("alias() response:", response.text)
    # print("success:", response.json()["result"]["success"])
    if "error" in response.json():
        print("API error:", response.json()["error"])
    return response.json()["result"]["success"]



# Give a blockchain an alias, a different name that can be used any place the blockchain’s ID is used.
# @ chainID: the blockchain’s ID (ex. "sV6o671RtkGBcno1FiaDbVcFv2sG5aVXMZYzKdP4VQAWmJQnM")
# @ alias: alias can now be used in place of the blockchain’s ID (in API endpoints, for example) (ex. "myBlockchainAlias")
def aliasChain(nodeAddr, chainID, alias):
    global requestID
    headers = {'content-type': 'application/json;'}
    requestID = requestID+1
    data = {"jsonrpc":"2.0", "id":requestID, "method" :"admin.aliasChain", "params": {"chain":chainID, "alias":alias}}
    response = requests.post(nodeAddr+ENDPOINT, headers=headers, data=json.dumps(data))
    # print("aliasChain() response:", response.text)
    # print("success:", response.json()["result"]["success"])
    if "error" in response.json():
        print("API error:", response.json()["error"])
    return response.json()["result"]["success"]



# Given a blockchain’s alias, get its ID (See avm.aliasChain for more context)
# @ chainAlias: chainID's alias by aliasChain() (ex. "X")
def getBlockchainID(nodeAddr, chainAlias):
    global requestID
    headers = {'content-type': 'application/json;'}
    requestID = requestID+1
    data = {"jsonrpc":"2.0", "id":requestID, "method" :"admin.getBlockchainID", "params": {"alias":chainAlias}}
    response = requests.post(nodeAddr+ENDPOINT, headers=headers, data=json.dumps(data))
    # print("getBlockchainID() response:", response.text)
    # print("blockchainID:", response.json()["result"]["blockchainID"])
    if "error" in response.json():
        print("API error:", response.json()["error"])
    return response.json()["result"]["blockchainID"]



# Start profiling the CPU utilization of the node. Will write the profile to the specified file on stop.
# @ fileName: the name of the file to write the profile to (ex. "cpu.profile")
def startCPUProfiler(nodeAddr, fileName):
    global requestID
    headers = {'content-type': 'application/json;'}
    requestID = requestID+1
    data = {"jsonrpc":"2.0", "id":requestID, "method" :"admin.startCPUProfiler", "params": {"fileName":fileName}}
    response = requests.post(nodeAddr+ENDPOINT, headers=headers, data=json.dumps(data))
    # print("startCPUProfiler() response:", response.text)
    # print("success:", response.json()["result"]["success"])
    if "error" in response.json():
        print("API error:", response.json()["error"])
    return response.json()["result"]["success"]



# Stop the CPU profile that was previously started
def stopCPUProfiler(nodeAddr):
    global requestID
    headers = {'content-type': 'application/json;'}
    requestID = requestID+1
    data = {"jsonrpc":"2.0", "id":requestID, "method" :"admin.stopCPUProfiler"}
    response = requests.post(nodeAddr+ENDPOINT, headers=headers, data=json.dumps(data))
    # print("stopCPUProfiler() response:", response.text)
    # print("success:", response.json()["result"]["success"])
    if "error" in response.json():
        print("API error:", response.json()["error"])
    return response.json()["result"]["success"]



# Dump the current memory footprint of the node to the specified file.
# @ fileName: the name of the file to write the profile to (ex. "mem.profile")
def memoryProfile(nodeAddr, fileName):
    global requestID
    headers = {'content-type': 'application/json;'}
    requestID = requestID+1
    data = {"jsonrpc":"2.0", "id":requestID, "method" :"admin.memoryProfile", "params": {"fileName":fileName}}
    response = requests.post(nodeAddr+ENDPOINT, headers=headers, data=json.dumps(data))
    # print("memoryProfile() response:", response.text)
    # print("success:", response.json()["result"]["success"])
    if "error" in response.json():
        print("API error:", response.json()["error"])
    return response.json()["result"]["success"]



# Dump the mutex statistics of the node to the specified file.
# @ fileName: the name of the file to dump the information into (ex. "lock.profile")
def lockProfile(nodeAddr, fileName):
    global requestID
    headers = {'content-type': 'application/json;'}
    requestID = requestID+1
    data = {"jsonrpc":"2.0", "id":requestID, "method" :"admin.lockProfile", "params": {"fileName":fileName}}
    response = requests.post(nodeAddr+ENDPOINT, headers=headers, data=json.dumps(data))
    # print("lockProfile() response:", response.text)
    # print("success:", response.json()["result"]["success"])
    if "error" in response.json():
        print("API error:", response.json()["error"])
    return response.json()["result"]["success"]



# get the node's ID (not included in the admin API document)
def getNodeID(nodeAddr):
    global requestID
    headers = {'content-type': 'application/json;'}
    requestID = requestID+1
    data = {"jsonrpc":"2.0", "id":requestID, "method" :"admin.getNodeID"}
    response = requests.post(nodeAddr+ENDPOINT, headers=headers, data=json.dumps(data))
    # print("getNodeID() response:", response.text)
    # print("nodeID:", response.json()["result"]["nodeID"])
    if "error" in response.json():
        print("API error:", response.json()["error"])
    return response.json()["result"]["nodeID"]


