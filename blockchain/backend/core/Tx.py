from Blockchain.Backend.core.Script import Script
class Tx:
    def __init__(self, version, tx_ins, tx_outs, locktime):
        self.version = version
        self.tx_ins = tx_ins  
        self.tx_outs = tx_outs
        self.locktime = locktime  
        
class TxIn:
    def __init__(self, prev_tx, prev_index, script_sig = None,  sequence=0xffffffff):
        self.prev_tx = prev_tx 
        self.prev_index = prev_index
        
        if script_sig is None:
            self.script_sig = Script()
        else:
            self.script_sig = script_sig 
        
        
        self.sequence = sequence
        
class TxOut:
    def __init__(self, amount, script_pubkey):
        self.amount = amount
        self.script_pubkey = script_pubkey
        