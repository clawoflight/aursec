from __future__ import print_function

import json
import datetime
import requests
import sys


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


class Block:
    def __init__(self, nr, block_hash, miner, time, transactions):
        self.nr = nr
        self.hash = block_hash
        self.miner = miner
        self.time = time
        self.transactions = transactions


class Blocks:
    def __init__(self):
        global all_blocks
        all_blocks = []
        self.url = "http://localhost:8105"
        self.headers = {'content-type': 'application/json'}
        payload = {
            "method": "eth_coinbase",
            "params": [],
            "jsonrpc": "2.0",
            "id": 1,
        }
        response = requests.post(
            self.url, data=json.dumps(payload), headers=self.headers).json()
        self.user = response["result"]

    def get_data(self, number):
        str_number = str(hex(number))
        payload = {
            "method": "eth_getBlockByNumber",
            "params": [str_number, True],
            "jsonrpc": "2.0",
            "id": 1,
        }

        response = requests.post(
            self.url, data=json.dumps(payload), headers=self.headers).json()
        miner = response["result"]["miner"]
        block_hash = response["result"]["hash"]
        time = datetime.datetime.fromtimestamp(int(response["result"]["timestamp"], 16)).strftime('%Y-%m-%d %H:%M:%S')
        number_transactions = len(response["result"]["transactions"])
        transactions = ""
        for i in range(0, number_transactions):
            transactions += self.json_result_to_string(response["result"]["transactions"][i])
            if i != number_transactions - 1:
                transactions += "\n"
        block = Block(number, block_hash, miner, time, transactions)
        all_blocks.append(block)

    def json_result_to_string(self, transaction):
        code = str(transaction["input"])
        if "0xcd79f86d" not in code:
            return "Transaction is no hash-commit"
        code = code[10:]
        first = int(code[1:64], 16)
        second = int(code[65:128], 16)
        len_id = int(code[first * 2:first * 2 + 64])
        id = bytearray.fromhex(code[(first * 2 + 64):(first * 2 + 64 + len_id * 2)]).decode().rstrip()
        len_hash = int(code[second * 2:second * 2 + 64])
        hash = bytearray.fromhex(code[(second * 2 + 64):(second * 2 + 64 + len_hash * 2)]).decode().rstrip()
        return "ID: " + id + " | Hash: " + hash

    def get_older_blocks(self, number, mine, transaction):
        blocks = all_blocks
        if mine and transaction:
            return [x for x in blocks if x.miner == self.user and x.transactions != "" and x.nr < number]
        elif mine:
            return [x for x in blocks if x.miner == self.user and x.nr < number]
        elif transaction:
            return [x for x in blocks if x.transactions != "" and x.nr < number]
        else:
            return [x for x in blocks if x.nr < number]


    def run(self, n):
        for x in range(n, 0, -1):
            self.get_data(x)

    def get_curr_block(self):
        payload = {
            "jsonrpc": "2.0",
            "method": "eth_blockNumber",
            "params": [],
            "id": 1
        }
        response = requests.post(
            self.url, data=json.dumps(payload), headers=self.headers).json()
        return int(response["result"], 16)
