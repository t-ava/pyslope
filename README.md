# Pyslopes - The AVA Platform Python Library

## Overview

Pyslopes is a Python Library for interfacing with the AVA Platform. The Pyslopes library allows one to issue commands to the AVA node APIs.

The APIs currently supported by default are:

* The AVA Virtual Machine (AVM) API
* The Keystore API
* The Admin API
* The Platform API

## Getting Started

We built Pyslopes with ease of use in mind. With this library, any Python developer is able to interact with a node on the AVA Platform who has enabled their API endpoints for the developer's consumption. We keep the library up-to-date with the latest changes in the [AVA Platform Specification](https://avalabs.org/docs/).

Using Pyslopes, developers are able to:

* Locally manage private keys
* Retrieve balances on addresses
* Get UTXOs for addresses
* Build and sign transactions
* Issue signed transactions to the AVM
* Create a subnetwork
* Administer a local node
* Retrieve AVA network information from a node

### Requirements

Pyslopes requires Python3.

### Installation

Just import Pyslopes files

```python
import sys
LIB_PATH = "/PATH/TO/PYSLOPES/pyslopes/src/apis"
sys.path.insert(1, LIB_PATH)
import admin, avm, keystore, platform_pchain
from admin import api as admin
from avm import api as avm
from keystore import api as keystore
from platform_pchain import api as platform
```

## Example &mdash; Sending An Asset

This example sends an asset in the AVM to a single recipient.

### Create users & keys

make users and keys to send & receive asset

```python
API_NODE_IP = "http://127.0.0.1:9650"
usernames = list(["user1", "user2"])
passwords = list(["POWERFUL_PASSWORD1", "POWERFUL_PASSWORD2"])
addresses = list()
for i in range(len(usernames)):
  keystore.createUser(API_NODE_IP, usernames[i], password[i])
  addresses.append(avm.createAddress(API_NODE_IP, usernames[i], passwords[i]))
```

### Get balances

check the balance of addresses

```python
for i in range(len(usernames)):
  print(usernames[i], addresses[i], "balance:", avm.getAllBalances(API_NODE_IP, addresses[i]))
```

### Send AVA

send AVA asset from user1 to user2

```python
avm.send(API_NODE_IP, 50000, "AVA", addresses[1], usernames[0], passwords[0], [addresses[0]])
```

