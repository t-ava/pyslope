import os, sys
LIB_PATH = "/home/jmlee/ava/Ava-RL-anche/pyslope/src/apis"
sys.path.insert(1, LIB_PATH)
import admin, avm, keystore, platform_pchain
from admin import api as admin
from avm import api as avm
from keystore import api as keystore
from platform_pchain import api as platform
import time

API_NODE_IP = "http://127.0.0.1:9650"

usernames = list(["user1", "user2", "user3"])
passwords = list(["jsdkbCJKEDleoi", "KDFNEobckav", "KDFNEobasfdkav-042!05"])
xAddresses = list(["X-JA6XmBq36MCy97Xi8kYBGbvu1B8Nhruxb", "X-MQPjxgthpTkXS8c3RAEJWtbTSZciULC8N", "X-PW2Bkxj4Hyc52o1AugXfP4FtLkyqM6qc7"])
privateKeys = list(["27v9G1abBD39z5S8P1A2oQHKMK5ND7JxfzKg2nHi7yxJv3rQ82", "2eEqN4Zsn5z3Qy13RjdAuxUoa8J2dXD6Zo9vS2osY68DLT6Y8E", "trUedHL6UDGLgv93yo6EcJ2UZiWhbiHjMCDU2ffJs9PcXvv3h"])

genesisPrivateKey = "ewoqjP7PxY4yr3iLTpLisriqt94hdyDFNgchSxGGztUrTXtNN"
genesisAddress = '6Y3kysjF9jnHnYkdS9yGAuoHyae2eNmeV'



# create users
def createUsers(usernames, passwords):
    if len(usernames) != len(passwords):
        print("createUser fail: different length")
        return

    for i in range(len(usernames)):
        try:
            print("create User:", keystore.createUser(API_NODE_IP, usernames[i], passwords[i]))
        except:
            print("api failed")



# create (control) P-chain key for users
def createPchainKeys(usernames, passwords):
    if len(usernames) != len(passwords):
        print("createPchainKeys fail: different length")
        return

    for i in range(len(usernames)):
        try:
            newAddress = platform.createAccount(API_NODE_IP, usernames[i], passwords[i], "")
            print("create P-chain key:", newAddress)
        except:
            print("api failed")
        print()



# create X-chain key for users
def createXchainKeys(usernames, passwords):
    if len(usernames) != len(passwords):
        print("createXchainKeys fail: different length")
        return

    for i in range(len(usernames)):
        try:
            newAddress = avm.createAddress(API_NODE_IP, usernames[i], passwords[i])
            print("create X-chain key:", newAddress)
            xAddresses[i] = newAddress
        except:
            print("api failed")
        print()



def createSubnet(addresses):
    # get the payerNonce
    try:
        account = platform.getAccount(API_NODE_IP, addresses[2])
        print("account:", account)
        payerNonce = int(account[1]) + 1
    except:
        print("api failed")
    print()

    # create the unsigned transaction to create subnet
    try:
        unsignedTx = platform.createSubnet(API_NODE_IP, addresses[:2], 2, payerNonce)
        print("unsigned tx to create subnet:", unsignedTx)
    except:
        print("api failed")
    print()

    # sign the unsigned tx
    try:
        signedTx = platform.sign(API_NODE_IP, unsignedTx, addresses[2], usernames[2], passwords[2])
        print("signed tx to create subnet:", signedTx)
    except:
        print("api failed")
    print()

    # issue the signed tx (broadcast the tx)
    try:
        txID = platform.issueTx(API_NODE_IP, signedTx)
        print("tx ID to create subnet:", txID)
    except:
        print("api failed")
    print()

    newSubnetID = txID
    return newSubnetID



# check the subnet exists
def checkSubnetExists():
    try:
        subnets = platform.getSubnets(API_NODE_IP)
        print("subnets:", subnets)
    except:
        print("api failed")
    print()



# get this node's ID
def getNodeID():
    try:
        nodeID = admin.getNodeID(API_NODE_IP)
        print("node ID:", nodeID)
        return nodeID
    except:
        print("api failed")
    print()



def addValidatorToNonDefaultSubnet(nodeID, subnetID, addresses):
    # get the payerNonce
    try:
        account = platform.getAccount(API_NODE_IP, addresses[2])
        print("account:", account)
        payerNonce = int(account[1]) + 1
    except:
        print("api failed")
    print()

    # create the unsigned transaction to add a validator to this subnet
    try:
        currentTime = int(time.time())+60
        duration = 86400    # CUASION: duration must be bigger than 24 hours (86400 sec) 
        print("nodeID:", nodeID, "subnetID:", subnetID, "startTime:", currentTime, "endTime:", currentTime+duration, "payerNonce:", payerNonce)
        unsignedTx = platform.addNonDefaultSubnetValidator(API_NODE_IP, nodeID, subnetID, currentTime, currentTime+duration, 1, payerNonce)
        print("unsignedTx:", unsignedTx)
    except:
        print("api failed")
    print()

    # sign the unsigned tx
    try:
        signedTx = platform.sign(API_NODE_IP, unsignedTx, addresses[0], usernames[0], passwords[0])
        print("partially signed tx to create subnet:", signedTx)
    except:
        print("api failed")
    print()
    try:
        signedTx = platform.sign(API_NODE_IP, signedTx, addresses[1], usernames[1], passwords[1])
        print("partially signed tx to create subnet:", signedTx)
    except:
        print("api failed")
    print()
    try:
        signedTx = platform.sign(API_NODE_IP, signedTx, addresses[2], usernames[2], passwords[2])
        print("fully signed tx to create subnet:", signedTx)
    except:
        print("api failed")
    print()

    # issue the signed tx (broadcast the tx)
    try:
        txID = platform.issueTx(API_NODE_IP, signedTx)
        print("tx ID to add validator to the subnet:", txID)
    except:
        print("api failed")
    print()



def addValidatorToDefaultSubnet(nodeID):
    # get the payerNonce
    try:
        account = platform.getAccount(API_NODE_IP, genesisAddress)
        print("account:", account)
        payerNonce = int(account[1]) + 1
    except:
        print("api failed")
    print()

    # create the unsigned transaction to add a validator to this subnet
    try:
        currentTime = int(time.time())+60
        duration = 90000 # must be bigger than 24 hours (86400 sec)
        unsignedTx = platform.addDefaultSubnetValidator(API_NODE_IP, nodeID, currentTime, currentTime+duration, 1000000, payerNonce, genesisAddress, 100000)
        print("unsignedTx:", unsignedTx)
    except:
        print("api failed")
    print()

    # sign the unsigned tx
    try:
        signedTx = platform.sign(API_NODE_IP, unsignedTx, genesisAddress, usernames[2], passwords[2])
        print("signed tx to create subnet:", signedTx)
    except:
        print("api failed")
    print()

    # issue the signed tx (broadcast the tx)
    try:
        txID = platform.issueTx(API_NODE_IP, signedTx)
        print("tx ID to add validator to the default subnet:", txID)
    except:
        print("api failed")
    print()



# check the validator is added to the subnet
def getSubnetValidator(subnetID):
    try:
        pendingValidators = platform.getPendingValidators(API_NODE_IP, subnetID)
        print("pending validators in the subnet:", pendingValidators)
        currentValidators = platform.getCurrentValidators(API_NODE_IP, subnetID)
        print("current validators in the subnet:", currentValidators)
    except:
        print("api failed")
    print()



# check the validator is added to the subnet
def getDefaultSubnetValidator():
    try:
        pendingValidators = platform.getPendingValidators(API_NODE_IP, "")
        print("pending validators in the default subnet:", pendingValidators)
        currentValidators = platform.getCurrentValidators(API_NODE_IP, "")
        print("current validators in the default subnet:", currentValidators)
    except:
        print("api failed")
    print()



def getBalance(address):
    try:
        print("all balances of", address, ":", platform.getAccount(API_NODE_IP, address))
    except:
        print("api failed")
    print()



def listAccounts(username, password):
    try:
        print("all accounts of", username, ":", platform.listAccounts(API_NODE_IP, username, password))
    except:
        print("api failed")
    print()



# get the genesis account which is funded already
def registerGenesisAccount():
    try:
        # hardcoded in https://github.com/ava-labs/gecko/blob/e5252c13e2df5c027852c08c883b30ea8e619ad3/genesis/config.go#L172
        # address: 6Y3kysjF9jnHnYkdS9yGAuoHyae2eNmeV
        defaultGenesisAccountPrivateKey = "ewoqjP7PxY4yr3iLTpLisriqt94hdyDFNgchSxGGztUrTXtNN"
        defaultGenesisAccount = platform.createAccount(API_NODE_IP, usernames[0], passwords[0], defaultGenesisAccountPrivateKey)
        print("create control key:", defaultGenesisAccount)
    except:
        print("api failed")
    print()



def createVariableCapAsset(assetName, assetSymbol):
    try:
        minterSets = list()
        minters = list([xAddresses[0]])
        minterSets.append({"minters":minters, "threshold":1})

        assetID = avm.createVariableCapAsset(API_NODE_IP, assetName, assetSymbol, 0, minterSets, usernames[0], passwords[0])
        return assetID
    except:
        print("api failed")



def mintAsset(amount, assetID):
    try:
        print("assetID::", assetID)
        minters = list([xAddresses[0]])
        unsignedTx = avm.createMintTx(API_NODE_IP, amount, assetID, xAddresses[0], minters)
        print("unsignedTx:", unsignedTx)
        return unsignedTx
    except:
        print("api failed")



def signMintTx(unsignedTx):
    try:
        signedTx = avm.signMintTx(API_NODE_IP, unsignedTx, xAddresses[0], usernames[0], passwords[0])
        print("signedTx:", signedTx)
        return signedTx
    except:
        print("api failed")



### main

try:
    admin.peers(API_NODE_IP)
except:
    print("\nERROR: run gecko node first (at avash -> $ runscript scripts/five_node_network.lua)\n")
    sys.exit()

print("wait for connection")
while len(admin.peers(API_NODE_IP)) < 4:
    pass
print("peers:", admin.peers(API_NODE_IP))

createUsers(usernames, passwords)
for i in range(3):
    address = avm.importKey(API_NODE_IP, usernames[i], passwords[i], privateKeys[i])
    print("imported address:", address)
address = avm.importKey(API_NODE_IP, usernames[0], passwords[0], genesisPrivateKey)
print("imported address:", address , "(genesis account imported)")

assetInfo = list()
assetInfo.append({"stationName": "station0", "stationSymbol": "ST0", "initialMintAmount": 100})
assetInfo.append({"stationName": "station1", "stationSymbol": "ST1", "initialMintAmount": 200})
assetInfo.append({"stationName": "station2", "stationSymbol": "ST2", "initialMintAmount": 300})

for i in range(len(assetInfo)):
    assetID = createVariableCapAsset(assetInfo[i]["stationName"], assetInfo[i]["stationSymbol"])
    print("wait for asset confirmation")
    time.sleep(3)
    unsignedTX = mintAsset(assetInfo[i]["initialMintAmount"], assetID)
    signedTx = signMintTx(unsignedTX)
    txID = avm.issueTx(API_NODE_IP, signedTx)
    print("txID:", txID)
    print("wait for tx comfirmation")
    while avm.getTxStatus(API_NODE_IP, txID) != "Accepted":
        pass
    print("tx status:", avm.getTxStatus(API_NODE_IP, txID))
    print("balance:", avm.getAllBalances(API_NODE_IP, xAddresses[0]))
    print("asset description:", avm.getAssetDescription(API_NODE_IP, assetID))

print("\nDone! make & mint all the assets")
print("current balance at address", xAddresses[0], "\n", avm.getAllBalances(API_NODE_IP, xAddresses[0]))
