import os, sys, random
LIB_PATH = "/home/jmlee/ava/pyslope/src/apis"
sys.path.insert(1, LIB_PATH)
import admin, avm, keystore, platform_pchain
from admin import api as admin
from avm import api as avm
from keystore import api as keystore
from platform_pchain import api as platform
import time

API_NODE_IP = "http://127.0.0.1:9650"

usernames = list(["genesis", "host", "user1"])
passwords = list(["jsdkbCJKEDleoi", "KDFNEobckav", "KDFNEobasfdkav-042!05"])
xAddresses = list(["X-6Y3kysjF9jnHnYkdS9yGAuoHyae2eNmeV", "X-MQPjxgthpTkXS8c3RAEJWtbTSZciULC8N", "X-PW2Bkxj4Hyc52o1AugXfP4FtLkyqM6qc7"])
privateKeys = list(["ewoqjP7PxY4yr3iLTpLisriqt94hdyDFNgchSxGGztUrTXtNN", "2eEqN4Zsn5z3Qy13RjdAuxUoa8J2dXD6Zo9vS2osY68DLT6Y8E", "trUedHL6UDGLgv93yo6EcJ2UZiWhbiHjMCDU2ffJs9PcXvv3h"])

genesisPrivateKey = "ewoqjP7PxY4yr3iLTpLisriqt94hdyDFNgchSxGGztUrTXtNN"
genesisAddress = '6Y3kysjF9jnHnYkdS9yGAuoHyae2eNmeV'

stationAddresses = list()
stationPrivateKeys = list()
initialRideNumber = list()



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



def createAndSaveKeys(username, password, addressNum, filename):
    f = open(filename, 'w')
    for i in range(addressNum):
        try:
            newAddress = avm.createAddress(API_NODE_IP, username, password)
            privateKey = avm.exportKey(API_NODE_IP, username, password, newAddress)
            log = newAddress + "," + privateKey + "\n"
            print("create X-chain key:", newAddress)
            print("private key:", privateKey)
            f.write(log)
        except:
            print("api failed")
        print()
    f.close()



def importAddressesFromFile(username, password, filename):
    f = open(filename, 'r')
    cnt = 0
    while True:
        line = f.readline()
        if not line: break
        address, privateKey = line.split(",")
        privateKey = privateKey[:-1]    # delete '\n'
        try:
            importedAddress = avm.importKey(API_NODE_IP, username, password, privateKey)
            print("imported address:", importedAddress)
            cnt = cnt + 1
            stationAddresses.append(importedAddress)
            stationPrivateKeys.append(privateKey)
        except:
            print("api failed")
    print("imported", cnt, "addresses successfully")
    f.close()



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



def createVariableCapAsset(assetName, assetSymbol):
    try:
        minterSets = list()
        minters = list([xAddresses[0]])
        minterSets.append({"minters":minters, "threshold":1})

        assetID = avm.createVariableCapAsset(API_NODE_IP, assetName, assetSymbol, 0, minterSets, usernames[0], passwords[0])
        return assetID
    except:
        print("api failed")



def mintAsset(amount, assetID, receiverAddr):
    try:
        print("assetID::", assetID)
        minters = list([xAddresses[0]])
        unsignedTx = avm.createMintTx(API_NODE_IP, amount, assetID, receiverAddr, minters)
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

# wait for the gecko nodes to be connected
try:
    admin.peers(API_NODE_IP)
except:
    print("\nERROR: run gecko node first (at avash -> $ runscript scripts/five_node_network.lua)\n")
    sys.exit()
print("wait for connection")
# while len(admin.peers(API_NODE_IP)) < 4:
#     pass
print("peers:", admin.peers(API_NODE_IP))

# make users
createUsers(usernames, passwords)

# import keys for genesis, host, user1
for i in range(len(usernames)):
    address = avm.importKey(API_NODE_IP, usernames[i], passwords[i], privateKeys[i])
    print("imported address:", address)

# get station addresses
# createAndSaveKeys(usernames[1], passwords[1], 969, "stations.txt") # if you dont have "stations.txt", then call this function
importAddressesFromFile(usernames[1], passwords[1], "stations_20.txt")

# make ride asset (asset ID: pePewnxEaP82Yd7cgnWbGUYgoBjvUwurvhzCLJpqusievGsUN)
assetID = createVariableCapAsset("ride", "RIDE")
print("wait for asset confirmation")
time.sleep(7)

# set station's initial amount of rides (between 5~15)
for i in range(len(stationAddresses)):
    randomInt = random.randint(5,15)
    initialRideNumber.append(randomInt)
print("sum of initialRideNumber:", sum(initialRideNumber))

# mint ride asset
unsignedTX = mintAsset(sum(initialRideNumber), assetID, xAddresses[1])
signedTx = signMintTx(unsignedTX)
txID = avm.issueTx(API_NODE_IP, signedTx)
print("txID:", txID)
print("wait for tx comfirmation")
while avm.getTxStatus(API_NODE_IP, txID) != "Accepted":
    pass
print("tx status:", avm.getTxStatus(API_NODE_IP, txID))
print("balance:", avm.getAllBalances(API_NODE_IP, xAddresses[1]))
print("asset description:", avm.getAssetDescription(API_NODE_IP, assetID))

# send ride asset to stations
for i in range(len(initialRideNumber)):
    try:
        avm.send(API_NODE_IP, initialRideNumber[i], assetID, stationAddresses[i], usernames[1], passwords[1], [xAddresses[1]])
        time.sleep(3)
    except:
        print("api failed")

# send AVA to host & user1 from genesis
avm.send(API_NODE_IP, 30000, "AVA", xAddresses[1], usernames[0], passwords[0], [xAddresses[0]])
time.sleep(1)
avm.send(API_NODE_IP, 20000, "AVA", xAddresses[2], usernames[0], passwords[0], [xAddresses[0]])
time.sleep(1)

# check balances
print("\nfinal result")
print(usernames[1], "balance:", avm.getAllBalances(API_NODE_IP, xAddresses[1]))
print(usernames[2], "balance:", avm.getAllBalances(API_NODE_IP, xAddresses[2]))
for i in range(len(initialRideNumber)):
    print("station balance:", avm.getAllBalances(API_NODE_IP, stationAddresses[i]))
