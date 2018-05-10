# Copyright (c) 2018 GenYuanLian

from p2pool.bitcoin import networks

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

PARENT = networks.nets['bitcoin']
SHARE_PERIOD = 30 # seconds,expected time to generate a share(always overhead)
CHAIN_LENGTH = 24*60*60//10 # shares,the number of shares p2pool keeps before discarding them
REAL_CHAIN_LENGTH = 24*60*60//10 # shares,sets the total number of previously found shares to include in the payout when a block is found
TARGET_LOOKBEHIND = 200 # shares,Determines the number of shares counted for difficulty regulation
SPREAD = 3 # blocks,determines how many blocks (max) to pay if a miner finds at lease one share
IDENTIFIER = 'fc70035c7a81bc6f'.decode('hex')
PREFIX = '2472ef181efcd37b'.decode('hex')
P2P_PORT = 9333
MIN_TARGET = 0
# MAX_TARGET = 2**256//2**32 - 1
# MAX_TARGET = 2**256//2**16 - 1
# MAX_TARGET = 2**256//2**25 - 1 #rbtc args
MAX_TARGET = 2**256//2**28 - 1   #scchain args
# MAX_TARGET = 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
# PERSIST = True
PERSIST = False
WORKER_PORT = 9332
BOOTSTRAP_ADDRS = ''.split(' ')#boostrap address that will autoconnect to
ANNOUNCE_CHANNEL = '#p2pool'
VERSION_CHECK = lambda v: None if 100000 <= v else 'Bitcoin version too old. Upgrade to 0.11.2 or newer!' # not a bug. BIP65 support is ensured by SOFTFORKS_REQUIRED
VERSION_WARNING = lambda v: None
SOFTFORKS_REQUIRED = set(['bip65', 'csv', 'segwit'])
MINIMUM_PROTOCOL_VERSION = 1600
NEW_MINIMUM_PROTOCOL_VERSION = 1700
SEGWIT_ACTIVATION_VERSION = 17
