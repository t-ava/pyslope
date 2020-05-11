import os, sys
LIB_PATH = "/home/jmlee/ava/Ava-RL-anche/pyslope/src/apis"
sys.path.insert(1, LIB_PATH)
import admin, avm, keystore, platform_pchain
from admin import api as admin
from avm import api as avm
from keystore import api as keystore
from platform_pchain import api as platform

API_NODE_IP = "http://127.0.0.1:9650"
usernames = list()
passwords = list()
usernames.append("tempUser")
passwords.append("fj!dbCJDSCB@A482v2b&e02")

print(admin.peers(API_NODE_IP))
print(platform.getBlockchains(API_NODE_IP))

try:
    print("create User:", keystore.createUser(API_NODE_IP, usernames[0], passwords[0]))
except:
    print("api failed")

try:
    print("create Address:", avm.createAddress(API_NODE_IP, usernames[0], passwords[0]))
except:
    print("api failed")
