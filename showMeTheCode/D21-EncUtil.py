import os
from hashlib import sha256
from hmac import HMAC
import hashlib
import base64

def hashSha256(password, salt=None):
    if salt is None:
        salt = os.urandom(8) # 64 bits.
    print(salt)
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
print(hashSha256(password.encode()))


#print(base64.decode(password))
#print(hashlib.algorithms_available)
#print(hashlib.sha256(password.encode("utf8")))
#print(hashSha256(password))
# print(hashWithSalt(password))

