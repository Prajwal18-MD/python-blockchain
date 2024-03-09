from Blockchain.Backend.util.util import decode_base58
from Blockchain.Backend.core.Script import Script
import time

class SendBTC:
    def __init__(self, fromAccount, toAccount,  Amount, UTXOS):
        self.COIN = 100000000
        self.FromPublicAddress = fromAccount
        self.toAccount = toAccount
        self.Amount = Amount *  self.COIN
        self.utxos = UTXOS
        
    def scriptPubKey(self, PublicAddress):
        h160 = decode_base58(PublicAddress)
        script_pubkey = Script().p2pkh_script(h160)
        return script_pubkey
        
    def prepareTxIn(self):
        TxIns = []
        self.Toatal = 0 
        
        self.From_address_script_pubkey = self.scriptPubKey(self.FromPublicAddress)
        self.fromPubKeyHash = self.From_address_script_pubkey.cmds[2]
        
        newutxos ={}
        
        try:
            while len(newutxos) < 1:
                newutxos = dict(self.utxos)
                time.sleep(2)
        except Exception as e:
            print(f"Error in converting the Managed Dict to Normal Dict")
    
    def prepareTxOut(self):
        pass
        
    def prepareTransaction(self):
        self.prepareTxIn()
        self.prepareTxOut()
        