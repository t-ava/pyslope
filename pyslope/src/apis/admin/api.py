import requests, json

ENDPOINT = "/ext/admin"

requestID = 0

def peers(nodeAddr):
    global requestID
    headers = {'content-type': 'application/json;',}

    requestID = requestID+1
    data = {"jsonrpc":"2.0", "id":requestID, "method" :"admin.peers"}
                        
    response = requests.post(nodeAddr+ENDPOINT, headers=headers, data=json.dumps(data))
                                
    print("res:", response.text)
    print("resDic:", response.json())
    print("peers:", response.json()["result"]["peers"])
    return response.json()["result"]["peers"]

print(peers('http://127.0.0.1:9650'))
print(peers('http://127.0.0.1:9650'))

