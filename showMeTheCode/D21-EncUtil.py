import os
from hashlib import sha256
from hmac import HMAC
import hashlib
import base64

#handle encode/decode encrypt/dycrypt hash,saltedHash
def hashWithSalt(password, salt=None):
    if salt is None:
        salt = os.urandom(8) # 64 bits.
    assert isinstance(password, str)
    result = HMAC(password, salt, sha256).digest()
    return salt + result

def hashSha256(password, salt=None):
    if salt is None:
        salt = os.urandom(8) # 64 bits.
    hash_object = hashlib.sha256(password + salt)
    hex_dig = hash_object.hexdigest()
    return hex_dig+":"+salt

def hashSha256WithNoSalt(password):
    hash_object = hashlib.sha256(password )
    hex_dig = hash_object.hexdigest()
    return hex_dig

password = 'password123'
print(base64.b64encode(password.encode()).decode('utf-8'))
print(base64.b64decode('cGFzc3dvcmQxMjM=').decode('UTF8'))
print(hashSha256WithNoSalt(password.encode()))


#print(base64.decode(password))
#print(hashlib.algorithms_available)
#print(hashlib.sha256(password.encode("utf8")))
#print(hashSha256(password))
# print(hashWithSalt(password))

