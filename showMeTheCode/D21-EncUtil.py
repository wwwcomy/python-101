import os
from hashlib import sha256
from hmac import HMAC
import hashlib
import base64

#use sha256 to hash the password with a salt, then return with the result with :base64Salt
def hashSha256(password, salt=None):
    if salt is None:
        salt = os.urandom(8) # 64 bits.
    print(salt)
    hash_object = hashlib.sha256(password + salt)
    hex_dig = hash_object.hexdigest()
    print(hex_dig)
    return hex_dig+":"+base64.b64encode(salt).decode('utf-8')
#check the input with base64 encoded salt, check equal with result
def checkHash(input, salt, result):
    print(salt)
    salt = base64.b64decode(salt)
    hash_object = hashlib.sha256(input + salt)
    hex_dig = hash_object.hexdigest()
    print(hex_dig)
    print(salt)
    return result==hex_dig

def hashSha256WithNoSalt(password):
    hash_object = hashlib.sha256(password )
    hex_dig = hash_object.hexdigest()
    return hex_dig
password = 'password123'
print(base64.b64encode(password.encode()).decode('utf-8'))
print(base64.b64decode('cGFzc3dvcmQxMjM=').decode('UTF8'))
print(hashSha256WithNoSalt(password.encode()))
hashedResult = hashSha256(password.encode())
print(hashedResult)
salt = hashedResult.split(':')[1]
print(salt)
print(checkHash(password.encode(),salt,hashedResult.split(':')[0]))


#print(base64.decode(password))
#print(hashlib.algorithms_available)
#print(hashlib.sha256(password.encode("utf8")))
#print(hashSha256(password))
# print(hashWithSalt(password))

