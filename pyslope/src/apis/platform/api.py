import requests, json

ENDPOINT = "/ext/P"
requestID = 0

# https://docs.ava.network/v1.0/en/api/platform/


def createBlockchain(nodeAddr, subnetID, vmID, name, payerNonce, genesisData):


    
def getBlockchainStatus(nodeAddr, blockchainID):

    
def createAccount(nodeAddr, username, password, privateKey):

    
def getAccount(nodeAddr, address, nonce, balance):

    
def listAccounts(nodeAddr, username, password):

    
def getCurrentValidators(nodeAddr, subnetID):

    
def getPendingValidators(nodeAddr, subnetID):

    
def sampleValidators(nodeAddr, size, subnetID):

    
def addDefaultSubnetValidator(nodeAddr, id, startTime, endTime, stakeAmount, payerNonce, destination, delegationFeeRate):

    
def addNonDefaultSubnetValidator(nodeAddr, id, subnetID, startTime, endTime, weight, payerNonce):

    
def addDefaultSubnetDelegator(nodeAddr, id, startTime, endTime, stakeAmount, payerNonce, destination):

    
def createSubnet(nodeAddr, controlKeys, threshold, payerNonce):


def validatedBy(nodeAddr, blockchainID):


    
def validates(nodeAddr, subnetID):


def getBlockchains(nodeAddr):


def exportAVA(nodeAddr, amount, to, payerNonce):


def importAVA(nodeAddr, to, payerNonce, username, password):


def sign(nodeAddr, tx, signer, username, password):


def issueTx(nodeAddr, tx):

