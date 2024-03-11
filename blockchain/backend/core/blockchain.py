import sys
sys.path.append('/Bitcoin')

from Blockchain.Backend.core.block import Block
from Blockchain.Backend.core.blockheader import BlockHeader
from Blockchain.Backend.util.util import hash256
from Blockchain.Backend.core.database.database import BlockchainDB
from Blockchain.Backend.core.Tx import CoinbaseTx
from multiprocessing import Process, Manager
from Blockchain.Frontend.run import main
import time



ZERO_HASH = '0' * 64
VERSION = 1

class Blockchain:
    def __init__(self , utxos):
        self.utxos = utxos
        
    def write_on_disk(self, block):
        blockchainDB = BlockchainDB()
        blockchainDB.write(block)
        
        
    def fetch_last_block(self):
        blockchainDB = BlockchainDB()
        return blockchainDB.lastBlock()
        
    
    def GenesisBlock(self):
        BlockHeight = 0
        prevBlockHash = ZERO_HASH
        self.addBlock(BlockHeight, prevBlockHash)
        
    def store_uxtos_in_cache(self):
        for tx in self.addTransactionsInBlock:
            print(f"Transaction added {tx.TxId} ")
            self.utxos[tx.TxId] = tx
    
    def addBlock(self, BlockHeight, prevBlockHash):
        timestamp = int(time.time())
        coinbaseInstance = CoinbaseTx(BlockHeight)
        coinbaseTx = coinbaseInstance.CoinbaseTransaction()
        merkelRoot = coinbaseTx.TxId
        bits = 'ffff001f'
        blockheader = BlockHeader(VERSION, prevBlockHash, merkelRoot, timestamp, bits)
        blockheader.mine()
        self.store_uxtos_in_cache(coinbaseTx)
        self.write_on_disk([Block(BlockHeight, 1, blockheader.__dict__, 1, coinbaseTx).__dict__])
        
        
    def main(self):
        lastBlock = self.fetch_last_block()
        if lastBlock is None:
            self.GenesisBlock()
       
        while True:
            lastBlock = self.fetch_last_block()
            BlockHeight = lastBlock["Height"] + 1
            prevBlockHash = lastBlock['BlockHeader']['blockHash']
            self.addBlock(BlockHeight,prevBlockHash)
        
if __name__ == "__main__":
    with Manager() as manager:
        utxos = manager.dict()
        
        webapp = Process(target = main, args =(utxos))
        webapp.start()
        
        blockchain = Blockchain(utxos)
        blockchain.main()
