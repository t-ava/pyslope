import requests, json

ENDPOINT = "/ext/bc/X"
# /ext/bc/blockchainID to interact with other AVM instances, where blockchainID is the ID of a blockchain running the AVM.

requestID = 0

# https://docs.ava.network/v1.0/en/api/avm/

# Create a new address controlled by the given user
def createAddress(nodeAddr, username, password):
    global requestID
    headers = {'content-type': 'application/json;'}
    requestID = requestID+1
    data = {"jsonrpc":"2.0", "id":requestID, "method" :"avm.createAddress", "params": {"username":username, "password":password}}
    response = requests.post(nodeAddr+ENDPOINT, headers=headers, data=json.dumps(data))
    # print("createAddress() response:", response.text)
    # print("address:", response.json()["result"]["address"])
    return response.json()["result"]["address"]



# Get the balance of an asset controlled by a given address
# @ address: (ex. "X-KqpU28P2ipUxfTfwaT847wWxyXB4XuWad")
# @ assetID: (ex. "2sLRGHdLCZkxKnAew9M91GcN4DWVP9WwSrLTYNTqdZAXFB57Py")
def getBalance(nodeAddr, address, assetID):
    global requestID
    headers = {'content-type': 'application/json;'}
    requestID = requestID+1
    data = {"jsonrpc":"2.0", "id":requestID, "method" :"avm.getBalance", "params": {"address":address, "assetID":assetID}}
    response = requests.post(nodeAddr+ENDPOINT, headers=headers, data=json.dumps(data))
    # print("getBalance() response:", response.text)
    # print("balance:", response.json()["result"]["balance"])
    return response.json()["result"]["balance"]


# Get the balances of all assets controlled by a given address
# @ address: (ex. "X-Go7PyA65ZUVichsQVmAt9d65h2S7Exiw")
# @ return type ex. balances: [{asset: "AVA", balance: "102"}, {asset: "2sdnziCz37Jov3QSNMXcFRGFJ1tgauaj6L7qfk7yUcRPfQMC79", balance: "1000"}]
def getAllBalances(nodeAddr, address):
    global requestID
    headers = {'content-type': 'application/json;'}
    requestID = requestID+1
    data = {"jsonrpc":"2.0", "id":requestID, "method" :"avm.getAllBalances", "params": {"address":address}}
    response = requests.post(nodeAddr+ENDPOINT, headers=headers, data=json.dumps(data))
    # print("getAllBalances() response:", response.text)
    # print("balances:", response.json()["result"]["balances"])
    return response.json()["result"]["balances"]



# Get the UTXOs that reference a given address
# UTXOs is a list of UTXO_IDs such that each UTXO references at least one address in addresses
# @ addresses: (ex. "X-xMrKg8uUECt5CS9RE9j5hizv2t2SWTbk")
# @ return type ex. utxos: ["3ng2kBneUGy8SY98FgNvEMPo2pgL7m9UqcTDbL4svzdNKiuTpQCewGeJyTqppjMjaimnAvQfVfBTWcy2Da2CAKMy9P3Pu6E4nqp7NbrNN1aptYTEGoeg6oMjV76QGiWn37RhFcWuboDLst778nemsE7RrNhccgnHAXCQ"]
def getUTXOs(nodeAddr, addresses):
    global requestID
    headers = {'content-type': 'application/json;'}
    requestID = requestID+1
    data = {"jsonrpc":"2.0", "id":requestID, "method" :"avm.getUTXOs", "params": {"addresses":addresses}}
    response = requests.post(nodeAddr+ENDPOINT, headers=headers, data=json.dumps(data))
    # print("getUTXOs() response:", response.text)
    # print("utxos:", response.json()["result"]["utxos"])
    return response.json()["result"]["utxos"]



# Send a signed transaction to the network
# @ tx: signed transaction (ex. "6sTENqXfk3gahxkJbEPsmX9eJTEFZRSRw83cRJqoHWBiaeAhVbz9QV4i6SLd6Dek4eLsojeR8FbT3arFtsGz9ycpHFaWHLX69edJPEmj2tPApsEqsFd7wDVp7fFxkG6HmySR")
# return type ex. txID: "NUPLwbt2hsYxpQg4H2o451hmTWQ4JZx2zMzM4SinwtHgAdX1JLPHXvWSXEnpecStLj"
def issueTx(nodeAddr, tx):
    global requestID
    headers = {'content-type': 'application/json;'}
    requestID = requestID+1
    data = {"jsonrpc":"2.0", "id":requestID, "method" :"avm.issueTx", "params": {"tx":tx}}
    response = requests.post(nodeAddr+ENDPOINT, headers=headers, data=json.dumps(data))
    # print("issueTx() response:", response.text)
    # print("txID:", response.json()["result"]["txID"])
    return response.json()["result"]["txID"]



# Sign an unsigned or partially signed transaction
# @ tx: an unsigned or partially signed mint transaction (ex. "1112yKaDdTb7XZXqX38X8U6ro7EC4GQdxDU48eHTcoQxPtJncHSQEMCi9n3hYaPp33K95i8sntkox5ZMHNq26DeNui4yuSQANXgFEeondXZvq65Pk1jnXbUpkJPkjX4KG1W9XQMAmCNpXs5xHzpX4THcYg3WY569Rj7cdf9Km4FQ3r3VDUAn1dpZLsCyQHeGb8Lr3ub7PGh4pn42KPAWsS6N4xCAGg1GGww2XNBxoDfu81toejPJFuqTJQg6tzgL82uT3amebb4FYQVU5B2gxH5Amevm1zsiTTfNDWui4BfB6e7jt8fc36UWYgb4MiaaApmySUe4ndt7SjFTT6taDkVNFdbUWuNEfiebrYFLpqL86mQ1XD")
# @ minter: the address signing this transaction (ex. "X-xMrKg8uUECt5CS9RE9j5hizv2t2SWTbk")
# @ username: the user that controls address minter (ex. "userThatControlsTheSignerAddress")
# @ password: password of the user username (ex. "myPassword")
def signMintTx(nodeAddr, tx, minter, username, password):
    global requestID
    headers = {'content-type': 'application/json;'}
    requestID = requestID+1
    data = {"jsonrpc":"2.0", "id":requestID, "method" :"avm.signMintTx", "params": {"tx":tx, "minter":minter, "username":username, "password":password}}
    response = requests.post(nodeAddr+ENDPOINT, headers=headers, data=json.dumps(data))
    # print("signMintTx() response:", response.text)
    # print("tx:", response.json()["result"]["tx"])
    return response.json()["result"]["tx"]



# Get the status of a transaction sent to the network
# @ txID: (ex. "2QouvFWUbjuySRxeX5xMbNCuAaKWfbk5FeEa2JmoF85RKLk2dD")
# @ return type ex. status: Accepted / Processing / Rejected / Unknown
#   Accepted: The transaction is (or will be) accepted by every node
#   Processing: The transaction is being voted on by this node
#   Rejected: The transaction will never be accepted by any node in the network
#   Unknown: The transaction hasn’t been seen by this node
def getTxStatus(nodeAddr, txID):
    global requestID
    headers = {'content-type': 'application/json;'}
    requestID = requestID+1
    data = {"jsonrpc":"2.0", "id":requestID, "method" :"avm.getTxStatus", "params": {"txID":txID}}
    response = requests.post(nodeAddr+ENDPOINT, headers=headers, data=json.dumps(data))
    # print("getTxStatus() response:", response.text)
    # print("status:", response.json()["result"]["status"])
    return response.json()["result"]["status"]


# Send a quantity of an asset to an address
# @ amount: asset amount to send (ex. 10000)
# @ assetID: ID of asset (ex. "AVA")
# @ to: address to receive asset (ex. "X-xMrKg8uUECt5CS9RE9j5hizv2t2SWTbk")
# @ username: asset is sent from addresses controlled by this user (ex. "userThatControlsAtLeast10000OfThisAsset")
# @ password: password of the user username (ex. "myPassword")
def send(nodeAddr, amount, assetID, to, username, password):
    global requestID
    headers = {'content-type': 'application/json;'}
    requestID = requestID+1
    data = {"jsonrpc":"2.0", "id":requestID, "method" :"avm.send", "params": {"amount":amount, "assetID":assetID, "to":to, "username":username, "password":password}}
    response = requests.post(nodeAddr+ENDPOINT, headers=headers, data=json.dumps(data))
    # print("send() response:", response.text)
    # print("txID:", response.json()["result"]["txID"])
    return response.json()["result"]["txID"]


# Create a new fixed-cap, fungible asset
# A quantity of it is created at initialization and then no more is ever created
# The asset can be sent with avm.sendFungibleAsset
# @ name: a human-readable name for the asset. Not necessarily unique (ex. "myFixedCapAsset")
# @ symbol: a shorthand symbol for the asset. Between 0 and 4 characters. Not necessarily unique. May be omitted (ex. "MFCA")
# @ denomination: determines how balances of this asset are displayed by user interfaces (ex. 1 -> display 100 as 10.0)
# @ initialHolders: Each element in initialHolders specifies that address holds amount units of the asset at genesis
#                 (ex. initialHolders: [{"address": "~~", "amount": 100}, {"address": "~~", "amount": 2000}])
# @ username: the user paying the fee (Since there are no transaction fees right now, you can leave username and password blank)
# @ password: password of the user username (ex. "myPassword")
def createFixedCapAsset(nodeAddr, name, symbol, denomination, initialHolders, username, password):
    global requestID
    headers = {'content-type': 'application/json;'}
    requestID = requestID+1
    data = {"jsonrpc":"2.0", "id":requestID, "method" :"avm.createFixedCapAsset", "params": {"name":name, "symbol":symbol, "denomination":denomination, "initialHolders":initialHolders, "username":username, "password":password}}
    response = requests.post(nodeAddr+ENDPOINT, headers=headers, data=json.dumps(data))
    # print("createFixedCapAsset() response:", response.text)
    # print("assetID:", response.json()["result"]["assetID"])
    return response.json()["result"]["assetID"]


# Create a new variable-cap, fungible asset. No units of the asset exist at initialization
# Minters can mint units of this asset using createMintTx, signMintTx and issueTx
# The asset can be sent with avm.send
# @ name: a human-readable name for the asset. Not necessarily unique (ex. "myFixedCapAsset")
# @ symbol: a shorthand symbol for the asset. Between 0 and 4 characters. Not necessarily unique. May be omitted (ex. "MFCA")
# @ denomination: determines how balances of this asset are displayed by user interfaces (ex. 1 -> display 100 as 10.0)
# @ minterSets: a list where each element specifies that threshold of the addresses in minters may together mint more of the asset by signing a minting transaction.
#                 (ex. minterSets: [{"minters": ["~~", "~~"], "threshold": 1}, {"minters": ["~~", "~~"], "threshold": 2}])
# @ username: the user paying the fee (Since there are no transaction fees right now, you can leave username and password blank)
# @ password: password of the user username (ex. "myPassword")
def createVariableCapAsset(nodeAddr, name, symbol, denomination, minterSets, username, password):
    global requestID
    headers = {'content-type': 'application/json;'}
    requestID = requestID+1
    data = {"jsonrpc":"2.0", "id":requestID, "method" :"avm.createVariableCapAsset", "params": {"name":name, "symbol":symbol, "denomination":denomination, "minterSets":minterSets, "username":username, "password":password}}
    response = requests.post(nodeAddr+ENDPOINT, headers=headers, data=json.dumps(data))
    # print("createVariableCapAsset() response:", response.text)
    # print("assetID:", response.json()["result"]["assetID"])
    return response.json()["result"]["assetID"]


# Create an unsigned transaction to mint more of a variable-cap asset (created with avm.createVariableCapAsset)
# @ amount: units of asset to be created
# @ assetID: ID of asset
# @ to: minted asset is controlled by this address
# @ minters: the minters that will sign this transaction before it’s issued
#         (len(minters) = threshold from one of this asset’s minter sets)
def createMintTx(nodeAddr, amount, assetID, to, minters):
    global requestID
    headers = {'content-type': 'application/json;'}
    requestID = requestID+1
    data = {"jsonrpc":"2.0", "id":requestID, "method" :"avm.createMintTx", "params": {"amount":amount, "assetID":assetID, "to":to, "minters":minters}}
    response = requests.post(nodeAddr+ENDPOINT, headers=headers, data=json.dumps(data))
    # print("createMintTx() response:", response.text)
    # print("tx:", response.json()["result"]["tx"])
    return response.json()["result"]["tx"]


# Get information about an asset
def getAssetDescription(nodeAddr, assetID):
    global requestID
    headers = {'content-type': 'application/json;'}
    requestID = requestID+1
    data = {"jsonrpc":"2.0", "id":requestID, "method" :"avm.getAssetDescription", "params": {"assetID":assetID}}
    response = requests.post(nodeAddr+ENDPOINT, headers=headers, data=json.dumps(data))
    # print("getAssetDescription() response:", response.text)
    # print("name:", response.json()["result"]["name"], "symbol:", response.json()["result"]["symbol"], "denomination:int:", response.json()["result"]["denomination:int"])
    return response.json()["result"]["name"], response.json()["result"]["symbol"], response.json()["result"]["denomination"], 


# ???
# Send AVA from the X-Chain to an account on the P-Chain
# After calling this method, you must call the P-Chain’s importAVA method to complete the transfer
# @ to: the ID of the P-Chain account the AVA is sent to
# @ amount: the amount of AVA to send.
# @ username: The AVA is sent from addresses controlled by the user username
# @ password: password of the user username (ex. "myPassword")
def exportAVA(nodeAddr, to, amount, username, password):
    global requestID
    headers = {'content-type': 'application/json;'}
    requestID = requestID+1
    data = {"jsonrpc":"2.0", "id":requestID, "method" :"avm.exportAVA", "params": {"to":to, "amount":amount, "username":username, "password":password}}
    response = requests.post(nodeAddr+ENDPOINT, headers=headers, data=json.dumps(data))
    # print("exportAVA() response:", response.text)
    # print("txID:", response.json()["result"]["txID"])
    return response.json()["result"]["txID"]



# ???
# Finalize a transfer of AVA from the P-Chain to the X-Chain
# Before this method is called, you must call the P-Chain’s exportAVA method to initiate the transfer
# @ to: the address the AVA is sent to
#       must be the same as the to argument in the corresponding call to the P-Chain’s exportAVA, 
#       except that the prepended X- should be included in this argument
# @ username: the user that controls to
# @ password: password of the user username (ex. "myPassword")
def importAVA(nodeAddr, to, username, password):
    global requestID
    headers = {'content-type': 'application/json;'}
    requestID = requestID+1
    data = {"jsonrpc":"2.0", "id":requestID, "method" :"avm.importAVA", "params": {"to":to, "username":username, "password":password}}
    response = requests.post(nodeAddr+ENDPOINT, headers=headers, data=json.dumps(data))
    # print("importAVA() response:", response.text)
    # print("txID:", response.json()["result"]["txID"])
    return response.json()["result"]["txID"]



# Get the private key that controls a given address
# The returned private key can be added to a user with avm.importKey
def exportKey(nodeAddr, username, password, address):
    global requestID
    headers = {'content-type': 'application/json;'}
    requestID = requestID+1
    data = {"jsonrpc":"2.0", "id":requestID, "method" :"avm.exportKey", "params": {"username":username, "password":password, "address":address}}
    response = requests.post(nodeAddr+ENDPOINT, headers=headers, data=json.dumps(data))
    # print("exportKey() response:", response.text)
    # print("privateKey:", response.json()["result"]["privateKey"])
    return response.json()["result"]["privateKey"]



# Give a user control over an address by providing the private key that controls the address
def importKey(nodeAddr, username, password, privateKey):
    global requestID
    headers = {'content-type': 'application/json;'}
    requestID = requestID+1
    data = {"jsonrpc":"2.0", "id":requestID, "method" :"avm.importKey", "params": {"username":username, "password":password, "privateKey":privateKey}}
    response = requests.post(nodeAddr+ENDPOINT, headers=headers, data=json.dumps(data))
    # print("importKey() response:", response.text)
    # print("address:", response.json()["result"]["address"])
    return response.json()["result"]["address"]



# Given a JSON representation of this Virtual Machine’s genesis state, create the byte representation of that state
# CAUSION: This call is made to the AVM’s static API endpoint "/ext/vm/avm"
def buildGenesis(nodeAddr, genesisData):
    global requestID
    headers = {'content-type': 'application/json;'}
    requestID = requestID+1
    data = {"jsonrpc":"2.0", "id":requestID, "method" :"avm.buildGenesis", "params": {"genesisData":genesisData}}
    response = requests.post(nodeAddr+"/ext/vm/avm", headers=headers, data=json.dumps(data))
    # print("buildGenesis() response:", response.text)
    # print("bytes:", response.json()["result"]["bytes"])
    return response.json()["result"]["bytes"]


