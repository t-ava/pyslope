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

usernames = list()
passwords = list()

usernames.append("user1")
usernames.append("user2")
usernames.append("user3")
passwords.append("jsdkbCJKEDleoi#$@t64dcla0")
passwords.append("KDFNEobckav-042!05")
passwords.append("KDFNEobasfdkav-042!05")



# create users
def createUsers():
    try:
        print("create User:", keystore.createUser(API_NODE_IP, usernames[0], passwords[0]))
    except:
        print("api failed")
    print()
    try:
        print("create User:", keystore.createUser(API_NODE_IP, usernames[1], passwords[1]))
    except:
        print("api failed")
    print()
    try:
        print("create User:", keystore.createUser(API_NODE_IP, usernames[2], passwords[2]))
    except:
        print("api failed")
    print()



# create control key for useres
addresses = list()
def createKeys():
    for i in range(3):
        addresses.append("")
        try:
            addresses[i] = platform.createAccount(API_NODE_IP, usernames[i], passwords[i], "")
            print("create control key:", addresses[i])
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



# get the information of the account in the p-chain
# try:
#     account = platform.getAccount(API_NODE_IP, addresses[2])
#     print("account:", account)
# except:
#     print("api failed")
# print()




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
        currentTime = int(time.time())+300
        duration = 6000 # 100min
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

    # try:
    #     txStatus = avm.getTxStatus(API_NODE_IP, txID)
    #     print("tx status:", txStatus)
    # except:
    #     print("api failed")
    # print()



# check the validator is added to the subnet
def getSubnetValidator(subnetID):
    try:
        pendingValidators = platform.getPendingValidators(API_NODE_IP, subnetID)
        print("pending validators in the subnet:", pendingValidators)
        currentValidators = platform.getCurrentValidators(API_NODE_IP, subnetID)
        print("current validators in the subnet:", pendingValidators)
    except:
        print("api failed")
    print()



def getBalance(address):
    try:
        print("all balances of", address, ":", platform.getAccount(API_NODE_IP, address))
    except:
        print("api failed")
    print()



### main

print("peers:", admin.peers(API_NODE_IP))

createUsers()

# createKeys()
# print("addresses:", addresses)

myAddresses = ['6UVvbsojmeLZGnrSUr8ohPvNgRvqXvL8D', 'Ejc5r6BscigQguBjYdAhjnFYbKheEYpEv', '5JFVr1cEh2ds3XuwNypsKfEgXGUZUTgAR']
# createSubnet(myAddresses)

# TODO: fund to P-chain account to add them in to the default subnet
# and then, maybe can add them to the custom subnet also
# https://docs.ava.network/v1.0/en/quickstart/ava-getting-started/#fund-your-p-chain-account
# https://github.com/ava-labs/gecko/blob/e5252c13e2df5c027852c08c883b30ea8e619ad3/genesis/genesis.go
getBalance(myAddresses[0])
getBalance(myAddresses[1])
getBalance(myAddresses[2])


checkSubnetExists()

mySubnetID = '2n2kVogRhTBXyZKwXT8kG61gPzCPymvSavpqvNQDJpyhKF1rgZ'
# addValidatorToNonDefaultSubnet(getNodeID(), mySubnetID, myAddresses)

getSubnetValidator(mySubnetID)

# blockchains = platform.getBlockchains(API_NODE_IP)
# print("blockchains:", blockchains)


print("DONE")


# GET GENESIS ACCOUNT which is FUNDED already !! 
try:
    # hardcoded in https://github.com/ava-labs/gecko/blob/e5252c13e2df5c027852c08c883b30ea8e619ad3/genesis/config.go#L172
    defaultGenesisAccountPrivateKey = "ewoqjP7PxY4yr3iLTpLisriqt94hdyDFNgchSxGGztUrTXtNN"
    defaultGenesisAccount = platform.createAccount(API_NODE_IP, usernames[0], passwords[0], defaultGenesisAccountPrivateKey)
    print("create control key:", defaultGenesisAccount)
except:
    print("api failed")
print()
getBalance(defaultGenesisAccount)



### TODO
# 1. find genesis account which was FUNDED already -> clear
# 2. add the node to the default subnet (need AVA)
# 3. make another subnet
# 4. add the node to the non-default subnet
# 5. make new X-blockchain

