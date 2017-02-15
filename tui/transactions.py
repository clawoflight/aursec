import json
import datetime
from pprint import pprint

class Transaction
	def __init__(self, nr, miner, sender, transaction)
		self.nr = nr
		self.miner = miner 
		self.sender = sender
		self.transaction = transaction


class Transactions
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





