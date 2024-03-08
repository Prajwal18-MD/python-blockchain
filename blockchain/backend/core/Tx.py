from Blockchain.Backend.core.Script import Script
from Blockchain.Backend.util.util import int_to_little_endian , bytes_needed, decode_base58

ZERO_HASH = b'\0' * 32
REWARD = 50

PRIVATE_KEY ='12581684044841109582091767466139305449310332399343515549215786231514462660173'
MINER_ADDRESS = '14XYBAcqUPMKCN65eI4VFNCLShVlF7bl4Z'

class CoinbaseTx:
    def __init__(self, BlockHeight):
        self.BlockHeightInLittleEndian = int_to_little_endian(BlockHeight , bytes_needed(BlockHeight))
        
    def CoinbaseTransaction(self):
        prev_tx = ZERO_HASH
        prev_index = 0xffffffff
        
        tx_ins = []
        tx_ins.append(TxIn(prev_tx , prev_index))
        tx_ins[0].script_sig.cmds.append(self.BlockHeightInLittleEndian)
        
        tx_outs = []
        target_amount = REWARD * 100000000
        target_h160 = decode_base58(MINER_ADDRESS)
        target_script = Script.p2pkh_script(target_h160)
        tx_outs.append(TxOut(amount = target_amount,  script_pubkey = target_script))
        
        return Tx(1, tx_ins, tx_outs, 0)


class Tx:
    def __init__(self, version, tx_ins, tx_outs, locktime):
        self.version = version
        self.tx_ins = tx_ins  
        self.tx_outs = tx_outs
        self.locktime = locktime
        
    def is_coinbase(self):
        if len(self.tx_ins) != 1 :
            return False
        
        first_input = self.tx_ins[0]
        
        if first_input.prev_tx != b'\x00' * 32:
            return False
        
        if first_input.prev_index != 0xffffffff:
            return False 
        
        return True
        
    def to_dict(self):
        
        if self.is_coinbase():
            self.tx_ins[0].prev_tx = self.tx_ins[0].prev_tx.hex()
            
          
        
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
        