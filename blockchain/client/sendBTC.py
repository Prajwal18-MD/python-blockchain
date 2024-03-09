from Blockchain.Backend.util.util import decode_base58
from Blockchain.Backend.core.Script import Script
from Blockchain.Backend.core.Tx import Tx, TxIn, TxOut
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
        self.Total = 0 
        
        self.From_address_script_pubkey = self.scriptPubKey(self.FromPublicAddress)
        self.fromPubKeyHash = self.From_address_script_pubkey.cmds[2]
        
        newutxos ={}
        
        try:
            while len(newutxos) < 1:
                newutxos = dict(self.utxos)
                time.sleep(2)
        except Exception as e:
            print(f"Error in converting the Managed Dict to Normal Dict")
            
        for Txbyte in  newutxos:
            if self.Total < self.Amount :
                TxObj = newutxos[Txbyte]
            
                for index, txout in enumerate(TxObj.tx_outs):
                    if txout.script_pubkey.cmds[2] == self.fromPubKeyHash:
                        self.Total += txout.amount
                        prev_tx = bytes.fromhex(TxObj.id())
                        TxIns.append(TxIn(prev_tx ,index))
            else:
                break
        
        if self.Total < self.Amount :
            self.isBalanceEnough = False
        return TxIns
            
        
    
    def prepareTxOut(self):
        TxOuts = []
        to_scriptPubkey = self.scriptPubKey(self.toAccount)
        TxOuts.append(TxOut(self.Amount, to_scriptPubkey))

        
        self.fee = self.COIN
        self.changeAmount = self.Total - self.Amount - self.fee
        TxOuts.append(TxOut(self.changeAmount, self.From_address_script_pubkey))
        return TxOuts
        
        
    def prepareTransaction(self):
       self.TxIns = self.prepareTxIn()
       self.TxOuts = self.prepareTxOut()
       self.TxObj = Tx(1, self.TxIns, self.TxOuts, 0)