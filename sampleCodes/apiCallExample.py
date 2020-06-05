import os, sys
LIB_PATH = "/home/jmlee/ava/pyslopes/src/apis"
sys.path.insert(1, LIB_PATH)
import admin, avm, keystore, platform_pchain
from admin import api as admin
from avm import api as avm
from keystore import api as keystore
from platform_pchain import api as platform

API_NODE_IP = "http://127.0.0.1:9650"
usernames = list()
passwords = list()
usernames.append("myUser")
passwords.append("fj!dbCJDSCB@A482v2b&e02")



### keystore API ### 

# 1. createUser(nodeAddr, username, password): create new user in the node
try:
    print("create User:", keystore.createUser(API_NODE_IP, usernames[0], passwords[0]))
except:
    print("api failed")
print()

# 2. listUsers(nodeAddr): get all users in the node
try:
    print("listUsers:", keystore.listUsers(API_NODE_IP))
except:
    print("api failed")
print()

# 3~4. export/import user function



### admin API ###

# 1. peers(nodeAddr): get all peers of the node
try:
    print("peers:", admin.peers(API_NODE_IP))
except:
    print("api failed")
print()

# 2. getNetworkID(nodeAddr): get the ID of the network
try:
    print("networkID:", admin.getNetworkID(API_NODE_IP))
except:
    print("api failed")
print()

# 3. aliasChain(nodeAddr, chainID, alias): aliasing blockchain (set alias instead of blockchainID)
try:
    print("alias chain success:", admin.aliasChain(API_NODE_IP,"4R5p2RXDGLqaifZE4hHWH9owe34pfoBULn1DrQTWivjg8o4aH", "myXChain"))
except:
    print("api failed")
print()

# 4. getBlockchainID(nodeAddr, chainAlias): get blockchain ID (give alias, get blockchainID)
try:
    print("blockchain ID:", admin.getBlockchainID(API_NODE_IP, "X"))
except:
    print("api failed")
try:
    print("blockchain ID:", admin.getBlockchainID(API_NODE_IP, "myXChain"))
except:
    print("api failed")
print()

# 5~8. profile functions



### avm API ###

# 1. createAddress(nodeAddr, username, password): create a new account to the user
try:
    newAddress = avm.createAddress(API_NODE_IP, usernames[0], passwords[0])
    newAddress2 = avm.createAddress(API_NODE_IP, usernames[0], passwords[0])
    print("new address address:", newAddress)
    print("new address address2:", newAddress2)
except:
    print("api failed")
print()

# 2. getBalance(nodeAddr, address, assetID): get balance of the account
try:
    print("balance (AVA):", avm.getBalance(API_NODE_IP, newAddress, "AVA"))
except:
    print("api failed")
print()

# 3. getAllBalances(nodeAddr, address): get all coins balance of the account
try:
    print("all balances:", avm.getAllBalances(API_NODE_IP, newAddress))
except:
    print("api failed")
print()

# 4. getUTXOs(nodeAddr, addresses): get utxos of the account
try:
    addresses = list()
    addresses.append(newAddress)
    print("utxos:", avm.getUTXOs(API_NODE_IP, addresses))
except:
    print("api failed")
print()

# 5. createFixedCapAsset(nodeAddr, name, symbol, denomination, initialHolders, username, password):
# make fixed-cap asset (= token which cannot be minted anymore)
try:
    initialHolders = list()
    holder1 = {"address": newAddress, "amount": 10000000}
    initialHolders.append(holder1)
    print("initialHolders:", initialHolders)
    fixedAssetID = avm.createFixedCapAsset(API_NODE_IP, "myFixedCapAsset", "MFCA", 0, initialHolders, usernames[0], passwords[0])
    print("fixed cap asset ID:", fixedAssetID)
except:
    print("api failed")
try:
    print("all balances:", avm.getAllBalances(API_NODE_IP, newAddress))
except:
    print("api failed")
try:
    print("balance (token):", avm.getBalance(API_NODE_IP, newAddress, fixedAssetID))
except:
    print("api failed")
print()

# 6. send(nodeAddr, amount, assetID, to, username, password): send asset
try:
    print("send tx ID:", avm.send(API_NODE_IP, 100, fixedAssetID, newAddress2, usernames[0], passwords[0]))
except:
    print("api failed")
print()

# 7. createVariableCapAsset(nodeAddr, name, symbol, denomination, minterSets, username, password):
# make variable-cap asset (= token which can be minted anytime)
try:
    minterSets = list()
    minters1 = list()
    minters1.append(newAddress)
    minter1 = {"minters":minters1, "threshold":1}
    minterSets.append(minter1)
    varAssetID = avm.createVariableCapAsset(API_NODE_IP, "myVariableCapAsset", "MVCA", 0, minterSets, usernames[0], passwords[0])
    print("variable cap asset ID:", varAssetID)
except:
    print("api failed")
print()

# 8. createMintTx(nodeAddr, amount, assetID, to, minters): make unsigned tx to mint var cap token
try:
    minters = list()
    minters.append(newAddress)
    mintTx = avm.createMintTx(API_NODE_IP, 10000, varAssetID, newAddress, minters)
    print("mint tx:", mintTx)
except:
    print("api failed")
print()



### platform API ###

# 1. getBlockchains(nodeAddr):
try:
    blockchains = platform.getBlockchains(API_NODE_IP)
    print("blockchains:", blockchains)
except:
    print("api failed")
print()

# 2. getBlockchainStatus(nodeAddr, blockchainID):
try:
    print("blockchain status:", platform.getBlockchainStatus(API_NODE_IP, blockchains[0]["id"]))
except:
    print("api failed")
print()

# 3. validatedBy(nodeAddr, blockchainID): get subnet ID of the blockchain
try:
    subnetID = platform.validatedBy(API_NODE_IP, blockchains[0]["id"])
    print("subnet ID:", subnetID)
except:
    print("api failed")
print()

# 4. def validates(nodeAddr, subnetID): get the IDs of the blockchains a Subnet validates
try:
    print("bockchain IDs:", platform.validates(API_NODE_IP, subnetID))
except:
    print("api failed")
print()

# 5. getCurrentValidators(nodeAddr, subnetID): get all validators of the subnet
try:
    print("validators of the subnet:", platform.getCurrentValidators(API_NODE_IP, subnetID))
except:
    print("api failed")
print()

# 6. getPendingValidators(nodeAddr, subnetID): get all validators candidates of the subnet
try:
    print("pending validators of the subnet:", platform.getPendingValidators(API_NODE_IP, subnetID))
except:
    print("api failed")
print()



# 7. listAccounts(nodeAddr, username, password): get all accounts of the user
try:
    print("addresses of the user:", platform.listAccounts(API_NODE_IP, usernames[0], passwords[0]))
except:
    print("api failed")
print()

