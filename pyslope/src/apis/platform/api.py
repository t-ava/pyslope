import requests, json

ENDPOINT = "/ext/P"
requestID = 0

# https://docs.ava.network/v1.0/en/api/platform/


# Create a new blockchain
# Currently only supports creation of new instances of the AVM and the Timestamp VM
# @ subnetID: the ID of the Subnet that validates the new blockchain
#           The Subnet must exist and can’t be the Default Subnet
# @ vmID: the ID of the Virtual Machine the blockchain runs. Can also be an alias of the Virtual Machine
# @ name: a human-readable name for the new blockchain. Not necessarily unique
# @ payerNonce: the next unused nonce of the account paying the transaction fee
# @ genesisData: the base 58 (with checksum) representation of the genesis state of the new blockchain
#             Virtual Machines should have a static API method named buildGenesis that can be used to generate genesisData
# @ unsignedTx: the unsigned transaction to create this blockchain
#             Must be signed by a sufficient number of the Subnet’s control keys and by the account paying the transaction fee
def createBlockchain(nodeAddr, subnetID, vmID, name, payerNonce, genesisData):
    global requestID
    headers = {'content-type': 'application/json;'}
    requestID = requestID+1
    data = {"jsonrpc":"2.0", "id":requestID, "method" :"platform.createBlockchain", "params": {"subnetID":subnetID, "vmID":vmID, "name":name, "payerNonce":payerNonce, "genesisData":genesisData}}
    response = requests.post(nodeAddr+ENDPOINT, headers=headers, data=json.dumps(data))
    # print("createBlockchain() response:", response.text)
    # print("unsignedTx:", response.json()["result"]["unsignedTx"])
    return response.json()["result"]["unsignedTx"]


# Get the status of a blockchain
# @ return type ex. status: Validating / Created / Preferred / Unknown
#     Validating: The blockchain is being validated by this node
#     Created: The blockchain exists but isn’t being validated by this node
#     Preferred: The blockchain was proposed to be created and is likely to be created but the transaction isn’t yet accepted
#     Unknown: The blockchain either wasn’t proposed or the proposal to create it isn’t preferred. The proposal may be resubmitted
def getBlockchainStatus(nodeAddr, blockchainID):
    global requestID
    headers = {'content-type': 'application/json;'}
    requestID = requestID+1
    data = {"jsonrpc":"2.0", "id":requestID, "method" :"platform.getBlockchainStatus", "params": {"subnetID":subnetID, "vmID":vmID, "name":name, "payerNonce":payerNonce, "genesisData":genesisData}}
    response = requests.post(nodeAddr+ENDPOINT, headers=headers, data=json.dumps(data))
    # print("getBlockchainStatus() response:", response.text)
    # print("status:", response.json()["result"]["status"])
    return response.json()["result"]["status"]



# The P-Chain uses an account model. This method creates an account
# @ username: the user that controls the new account.
# @ password: user’s password.
# @ privateKey: the private key that controls the account.
#               If omitted, a new private key is generated.
# @ return type ex. address: the address of the newly created account
def createAccount(nodeAddr, username, password, privateKey):
    global requestID
    headers = {'content-type': 'application/json;'}
    requestID = requestID+1
    data = {"jsonrpc":"2.0", "id":requestID, "method" :"platform.createAccount", "params": {"username":username, "password":password, "privateKey":privateKey}}
    response = requests.post(nodeAddr+ENDPOINT, headers=headers, data=json.dumps(data))
    # print("createAccount() response:", response.text)
    # print("address:", response.json()["result"]["address"])
    return response.json()["result"]["address"]



The P-Chain uses an account model. An account is identified by an address
This method returns the account with the given address
# @ address: the account’s address.
# @ return type ex. nonce: the account’s most recently used nonce.
# @ return type ex. balance: the account’s balance in nAVA.
def getAccount(nodeAddr, address):
    global requestID
    headers = {'content-type': 'application/json;'}
    requestID = requestID+1
    data = {"jsonrpc":"2.0", "id":requestID, "method" :"platform.getAccount", "params": {"address":address}}
    response = requests.post(nodeAddr+ENDPOINT, headers=headers, data=json.dumps(data))
    # print("getAccount() response:", response.text)
    # print("address:", response.json()["result"]["address"], "nonce:", response.json()["result"]["nonce"], "balance:", response.json()["result"]["balance"])
    return response.json()["result"]["address"], response.json()["result"]["nonce"], response.json()["result"]["balance"]



# List the accounts controlled by the specified user
# @ return type ex. accounts: [{address: "~~~", nonce: ~, balance: ~}, {address: "~~~", nonce: ~, balance: ~}]
def listAccounts(nodeAddr, username, password):
    global requestID
    headers = {'content-type': 'application/json;'}
    requestID = requestID+1
    data = {"jsonrpc":"2.0", "id":requestID, "method" :"platform.listAccounts", "params": {"username":username, "password":password}}
    response = requests.post(nodeAddr+ENDPOINT, headers=headers, data=json.dumps(data))
    # print("listAccounts() response:", response.text)
    # print("accounts:", response.json()["result"]["accounts"])
    return response.json()["result"]["accounts"]



# List the current validators of the given Subnet
# @ subnetID: the subnet whose current validators are returned
#             If omitted, returns the current validators of the Default Subnet
# @ return type ex. validators[i]: {startTime, endTime, weight, stakeAmount, id}
#   startTime: the Unix time when the validator starts validating the Subnet
#   endTime: the Unix time when the validator stops validating the Subnet
#   weight: the validator’s weight when sampling validators. Omitted if subnetID is the default subnet
#   stakeAmount: the amount of nAVA this validator staked. Omitted if subnetID is not the default subnet
#   id: the validator’s ID
def getCurrentValidators(nodeAddr, subnetID):
    global requestID
    headers = {'content-type': 'application/json;'}
    requestID = requestID+1
    data = {"jsonrpc":"2.0", "id":requestID, "method" :"platform.getCurrentValidators", "params": {"subnetID":subnetID}}
    response = requests.post(nodeAddr+ENDPOINT, headers=headers, data=json.dumps(data))
    # print("getCurrentValidators() response:", response.text)
    # print("validators:", response.json()["result"]["validators"])
    return response.json()["result"]["validators"]



# List the validators in the pending validator set of the specified Subnet
# Each validator is not currently validating the Subnet but will in the future
def getPendingValidators(nodeAddr, subnetID):
    global requestID
    headers = {'content-type': 'application/json;'}
    requestID = requestID+1
    data = {"jsonrpc":"2.0", "id":requestID, "method" :"platform.getPendingValidators", "params": {"subnetID":subnetID}}
    response = requests.post(nodeAddr+ENDPOINT, headers=headers, data=json.dumps(data))
    # print("getPendingValidators() response:", response.text)
    # print("validators:", response.json()["result"]["validators"])
    return response.json()["result"]["validators"]



# Sample validators from the specified Subnet
# @ size: the number of validators to sample.
# @ subnetID: the Subnet to sampled from. If omitted, defaults to the Default Subnet
# @ return type ex. validators: Each element is the ID of a validator
def sampleValidators(nodeAddr, size, subnetID):
    global requestID
    headers = {'content-type': 'application/json;'}
    requestID = requestID+1
    data = {"jsonrpc":"2.0", "id":requestID, "method" :"platform.sampleValidators", "params": {"size":size, "subnetID":subnetID}}
    response = requests.post(nodeAddr+ENDPOINT, headers=headers, data=json.dumps(data))
    # print("sampleValidators() response:", response.text)
    # print("validators:", response.json()["result"]["validators"])
    return response.json()["result"]["validators"]


# Add a validator to the Default Subnet
# @ id: the node ID of the validator
# @ startTime: the Unix time when the validator starts validating the Default Subnet
# @ endTime: the Unix time when the validator stops validating the Default Subnet (and staked AVA is returned)
# @ stakeAmount: the amount of nAVA the validator is staking
# @ payerNonce: the next unused nonce of the account that is providing the staked AVA and paying the transaction fee
# @ destination: the address of the account that the staked AVA will be returned to, as well as a validation reward if the validator is sufficiently responsive and correct while it validated
# @ delegationFeeRate: the percent fee this validator charges when others delegate stake to them, multiplied by 10,000
#                     For example, suppose a validator has delegationFeeRate 300,000 and someone delegates to that validator
#                     When the delegation period is over, if the delegator is entitled to a reward, 30% of the reward (300,000 / 10,000) goes to the validator and 70% goes to the delegato
# @ return type ex. unsignedTx: the the unsigned transaction. It must be signed (using sign) by the key of the account providing the staked AVA/paying the transaction fee before it can be issued
def addDefaultSubnetValidator(nodeAddr, id, startTime, endTime, stakeAmount, payerNonce, destination, delegationFeeRate):
    global requestID
    headers = {'content-type': 'application/json;'}
    requestID = requestID+1
    data = {"jsonrpc":"2.0", "id":requestID, "method" :"platform.addDefaultSubnetValidator", "params": {"id":id, "startTime":startTime, "endTime":endTime, "stakeAmount":stakeAmount, "payerNonce":payerNonce, "destination":destination, "delegationFeeRate":delegationFeeRate}}
    response = requests.post(nodeAddr+ENDPOINT, headers=headers, data=json.dumps(data))
    # print("addDefaultSubnetValidator() response:", response.text)
    # print("unsignedTx:", response.json()["result"]["unsignedTx"])
    return response.json()["result"]["unsignedTx"]



# Add a validator to a Subnet other than the Default Subnet
# The validator must validate the Default Subnet for the entire duration they validate this Subnet
# @ id: the node ID of the validator
# @ subnetID: the Subnet they will validate
# @ startTime: the Unix time when the validator starts validating the Subnet
# @ endTime: the Unix time when the validator stops validating the Subnet
# @ weight: the validator’s weight used for sampling
# @ payerNonce: the next unused nonce of the account that will pay the transaction fee for this transaction
# @ return type ex. unsignedTx: the unsigned transaction
#     It must be signed (using sign) by the proper number of the Subnet’s control keys 
#     and by the key of the account paying the transaction fee before it can be issued
def addNonDefaultSubnetValidator(nodeAddr, id, subnetID, startTime, endTime, weight, payerNonce):
    global requestID
    headers = {'content-type': 'application/json;'}
    requestID = requestID+1
    data = {"jsonrpc":"2.0", "id":requestID, "method" :"platform.addNonDefaultSubnetValidator", "params": {"id":id, "subnetID":subnetID, "startTime":startTime, "endTime":endTime, "weight":weight, "payerNonce":payerNonce}}
    response = requests.post(nodeAddr+ENDPOINT, headers=headers, data=json.dumps(data))
    # print("addNonDefaultSubnetValidator() response:", response.text)
    # print("unsignedTx:", response.json()["result"]["unsignedTx"])
    return response.json()["result"]["unsignedTx"]



# Add a delegator to the Default Subnet
# A delegator stakes AVA and specifies a validator (the delegatee) to validate on their behalf
# The delegatee has an increased probability of being sampled by other validators (weight) in proportion to the stake delegated to them
# The delegatee charges a fee to the delegator; the former receives a percentage of the delegator’s validation reward (if any)
# The delegation period must be a subset of the perdiod that the delegatee validates the Default Subnet
def addDefaultSubnetDelegator(nodeAddr, id, startTime, endTime, stakeAmount, payerNonce, destination):
    global requestID
    headers = {'content-type': 'application/json;'}
    requestID = requestID+1
    data = {"jsonrpc":"2.0", "id":requestID, "method" :"platform.addDefaultSubnetDelegator", "params": {"id":id, "startTime":startTime, "endTime":endTime, "stakeAmount":stakeAmount, "payerNonce":payerNonce, "destination":destination}}
    response = requests.post(nodeAddr+ENDPOINT, headers=headers, data=json.dumps(data))
    # print("addDefaultSubnetDelegator() response:", response.text)
    # print("unsignedTx:", response.json()["result"]["unsignedTx"])
    return response.json()["result"]["unsignedTx"]



# Create an unsigned transaction to create a new Subnet
# The unsigned transaction must be signed with the key of the account paying the transaction fee
# The Subnet’s ID is the ID of the transaction that creates it (ex. the response from issueTx when issuing the signed transaction)
def createSubnet(nodeAddr, controlKeys, threshold, payerNonce):
    global requestID
    headers = {'content-type': 'application/json;'}
    requestID = requestID+1
    data = {"jsonrpc":"2.0", "id":requestID, "method" :"platform.createSubnet", "params": {"controlKeys":controlKeys, "threshold":threshold, "payerNonce":payerNonce}}
    response = requests.post(nodeAddr+ENDPOINT, headers=headers, data=json.dumps(data))
    # print("createSubnet() response:", response.text)
    # print("unsignedTx:", response.json()["result"]["unsignedTx"])
    return response.json()["result"]["unsignedTx"]



# Get the Subnet that validates a given blockchain
# @ blockchainID: the blockchain’s ID
# @ return type ex. subnetID: the ID of the Subnet that validates the blockchain
def validatedBy(nodeAddr, blockchainID):
    global requestID
    headers = {'content-type': 'application/json;'}
    requestID = requestID+1
    data = {"jsonrpc":"2.0", "id":requestID, "method" :"platform.validatedBy", "params": {"blockchainID":blockchainID}}
    response = requests.post(nodeAddr+ENDPOINT, headers=headers, data=json.dumps(data))
    # print("validatedBy() response:", response.text)
    # print("subnetID:", response.json()["result"]["subnetID"])
    return response.json()["result"]["subnetID"]



# Get the IDs of the blockchains a Subnet validates
# @ subnetID: the Subnet’s ID
# @ return type ex. blockchainIDs: Each element is the ID of a blockchain the Subnet validates
def validates(nodeAddr, subnetID):
    global requestID
    headers = {'content-type': 'application/json;'}
    requestID = requestID+1
    data = {"jsonrpc":"2.0", "id":requestID, "method" :"platform.validates", "params": {"subnetID":subnetID}}
    response = requests.post(nodeAddr+ENDPOINT, headers=headers, data=json.dumps(data))
    # print("validates() response:", response.text)
    # print("blockchainIDs:", response.json()["result"]["blockchainIDs"])
    return response.json()["result"]["blockchainIDs"]



# Get all the blockchains that exist (excluding the P-Chain)
# @ return type ex. blockchains: all of the blockchains that exists on the AVA network
# @   ex. blockchains[i]: {id, subnetID, vmID}
# @   id: the blockchain’s ID.
# @   subnetID: the ID of the Subnet that validates this blockchain.
# @   vmID: the ID of the Virtual Machine the blockchain runs.
def getBlockchains(nodeAddr):
    global requestID
    headers = {'content-type': 'application/json;'}
    requestID = requestID+1
    data = {"jsonrpc":"2.0", "id":requestID, "method" :"platform.getBlockchains", "params": {"subnetID":subnetID}}
    response = requests.post(nodeAddr+ENDPOINT, headers=headers, data=json.dumps(data))
    # print("getBlockchains() response:", response.text)
    # print("blockchains:", response.json()["result"]["blockchains"])
    return response.json()["result"]["blockchains"]



# Send AVA from an account on the P-Chain to an address on the X-Chain
# This transaction must be signed with the key of the account that the AVA is sent from and which pays the transaction fee
# After issuing this transaction, you must call the X-Chain’s importAVA method to complete the transfer
def exportAVA(nodeAddr, amount, to, payerNonce):
    global requestID
    headers = {'content-type': 'application/json;'}
    requestID = requestID+1
    data = {"jsonrpc":"2.0", "id":requestID, "method" :"platform.exportAVA", "params": {"amount":amount, "to":to, "payerNonce":payerNonce}}
    response = requests.post(nodeAddr+ENDPOINT, headers=headers, data=json.dumps(data))
    # print("exportAVA() response:", response.text)
    # print("unsignedTx:", response.json()["result"]["unsignedTx"])
    return response.json()["result"]["unsignedTx"]



# Complete a transfer of AVA from the X-Chain to the P-Chain
# Before this method is called, you must call the X-Chain’s exportAVA method to initiate the transfer
def importAVA(nodeAddr, to, payerNonce, username, password):
    global requestID
    headers = {'content-type': 'application/json;'}
    requestID = requestID+1
    data = {"jsonrpc":"2.0", "id":requestID, "method" :"platform.importAVA", "params": {"to":to, "payerNonce":payerNonce, "username":username, "password":password}}
    response = requests.post(nodeAddr+ENDPOINT, headers=headers, data=json.dumps(data))
    # print("importAVA() response:", response.text)
    # print("tx:", response.json()["result"]["tx"])
    return response.json()["result"]["tx"]



# Sign an unsigned or partially signed transaction
# Transactions to add non-default Subnets require signatures from control keys and from the account paying the transaction fee
# If signer is a control key and the transaction needs more signatures from control keys, sign will provide a control signature
# Otherwise, signer will sign to pay the transaction fee
def sign(nodeAddr, tx, signer, username, password):
    global requestID
    headers = {'content-type': 'application/json;'}
    requestID = requestID+1
    data = {"jsonrpc":"2.0", "id":requestID, "method" :"platform.sign", "params": {"tx":tx, "signer":signer, "username":username, "password":password}}
    response = requests.post(nodeAddr+ENDPOINT, headers=headers, data=json.dumps(data))
    # print("sign() response:", response.text)
    # print("tx:", response.json()["result"]["tx"])
    return response.json()["result"]["tx"]



# Issue a transaction to the Platform Chain
# @ tx: the base 58 (with checksum) representation of a transaction
# @ return type ex. txID: the transaction’s ID
def issueTx(nodeAddr, tx):
    global requestID
    headers = {'content-type': 'application/json;'}
    requestID = requestID+1
    data = {"jsonrpc":"2.0", "id":requestID, "method" :"platform.issueTx", "params": {"tx":tx}}
    response = requests.post(nodeAddr+ENDPOINT, headers=headers, data=json.dumps(data))
    # print("issueTx() response:", response.text)
    # print("txID:", response.json()["result"]["txID"])
    return response.json()["result"]["txID"]
