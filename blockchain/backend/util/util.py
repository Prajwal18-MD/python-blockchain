import hashlib

def hash256(s):
    return  hashlib.sha256(hashlib.sha256(s).digest()).digest()