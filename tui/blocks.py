import json
import datetime
from pprint import pprint

class Block
	def __init__(self, nr, miner, sender, transaction)
		self.nr = nr
		self.miner = miner 
		self.sender = sender
		self.transaction = transaction


class Blocks
 	def __init__ (self)
 	 	self.all_blocks = []
 	 	self.mine_blocks = []
 	 	self.transactions = []
 		self.url = "http://localhost:8105"
 		self.localhostheaders = {'content-type': 'application/json'}
 		payload = {
	        "method": "eth_coinbase",
	        "params": [],
	        "jsonrpc": "2.0",
	        "id": 1,
	    }
 		response = requests.post(
	        self.url, data=json.dumps(payload), headers=self.headers).json()
 		self.user = response["result"]

    
	    

 	def get_data(self, number)
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
	    time = datetime.datetime.fromtimestamp(int(response["result"]["timestamp"],16)).strftime('%Y-%m-%d %H:%M:%S')
	    number_transactions = len(response["result"]["transactions"])
	    transactions = ""
	    for i in xrange(0,number_transactions):
	    	transaction += json_result_to_string(["result"]["transactions"][i])
	    	if i != number_transactions-1:
	    		transactions += " | "
	    block = Block(number,miner,sender,transactions)
	    self.all_blocks.append(block)
	    if(miner == self.user)
	    	self.mine_blocks.append(block)
	    if(number_transactions != 0)
	    	self.transactions.append(block)

	def json_result_to_string(self,transaction)
		code = str(transaction["input"])[10:]
		first = int(code[1:64],16)
		second = int(code [65:128],16)
		len_id = int(code[first*2:first*2+64])
		id=bytearray.fromhex(code[(first*2+64):(first*2+64+len_id*2)]).decode().rstrip()
		len_hash = int(code[second*2:second*2+64])
		hash=bytearray.fromhex(code[(second*2+64):(second*2+64+len_hash*2)]).decode().rstrip()
		return ("ID: " + id +" hash: " + hash)





