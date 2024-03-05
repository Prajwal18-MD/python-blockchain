class Block:
    
    def __init__(self, Height, Blocksize, BlockHeader, TxCount, Txs):
        self.Height = Height
        self.BlockSize = Blocksize
        self.BlockHeader = BlockHeader
        self.Txcount = TxCount
        self.Txs = Txs