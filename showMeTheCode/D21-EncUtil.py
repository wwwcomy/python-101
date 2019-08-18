import os
from hashlib import sha256
from hmac import HMAC
import hashlib
import base64
import binascii
from Crypto.Cipher import AES


# pip install pycryptodome

# use sha256 to hash the password with a salt, then return with the result with :base64Salt
def hashSha256(password, salt=None):
    if salt is None:
        salt = os.urandom(8)  # 64 bits.
    print(salt)
    hash_object = hashlib.sha256(password + salt)
    hex_dig = hash_object.hexdigest()
    print(hex_dig)
    # here I'm using base64 encode to handle the bytes
    # after analyzing, bytes can cast to string using str()
    # using encode will cause un-recogonized code error
    # while cast string back to string, use eval()

    return hex_dig + ":" + base64.b64encode(salt).decode('utf-8')


# check the input with base64 encoded salt, check equal with result
def checkHash(input, salt, result):
    print(salt)
    salt = base64.b64decode(salt)
    hash_object = hashlib.sha256(input + salt)
    hex_dig = hash_object.hexdigest()
    print(hex_dig)
    print(salt)
    return result == hex_dig


def hashSha256WithNoSalt(password):
    hash_object = hashlib.sha256(password)
    hex_dig = hash_object.hexdigest()
    return hex_dig


def createSalt(salt=None):
    if salt is None:
        salt = os.urandom(8)  # 64 bits.
    print(salt)
    print(type(salt))
    sSalt = str(salt)
    print(sSalt)
    print(type(sSalt))

    revertSalt = eval(sSalt)
    print(revertSalt)
    print(type(revertSalt))

    hexlifiedSalt = binascii.hexlify(salt)
    print(hexlifiedSalt)
    print(hexlifiedSalt.decode())

    unhexlifiedSalt = binascii.unhexlify(hexlifiedSalt)
    print(unhexlifiedSalt)


def encrypt(input):
    key = b'Thesafestkey....'
    # looks like only ECB mode works
    # TODO spend some time on checking the difference of the mode
    cipher = AES.new(key, AES.MODE_ECB)
    input = add_to_16(input)
    print(input)
    # ciphertext, tag = cipher.encrypt_and_digest(input.encode())
    encResult = cipher.encrypt(input)
    print("encResult as bytes:")
    print(encResult)
    return binascii.hexlify(encResult)
    #return base64.b64encode(encResult).decode('utf-8')

def add_to_16(s):
    while len(s) % 16 != 0:
        s += '\0'
    return str.encode(s)
    #return s.encode()


def dycrypt(input):
    key = b'Thesafestkey....'
    cipher = AES.new(key, AES.MODE_ECB)
    # print(unhexlify)
    print(input)
    #tmp =  base64.b64decode(input)
    tmp = binascii.unhexlify(input)
    print(tmp)
    decrypted_text = cipher.decrypt(tmp).rstrip(b'\0')
    return decrypted_text.decode()


print('******* This is for Create Salt *********')
createSalt()
password = 'password123'

print('******* This is for Base64 *********')
print(base64.b64encode(password.encode()).decode('utf-8'))
print(base64.b64decode('cGFzc3dvcmQxMjM=').decode('UTF8'))

print('******* This is for Hash *********')
print(hashSha256WithNoSalt(password.encode()))
hashedResult = hashSha256(password.encode())
print('Hash with salt:' + hashedResult)
salt = hashedResult.split(':')[1]
print('Salt is:' + salt)
print(checkHash(password.encode(), salt, hashedResult.split(':')[0]))

print('******* This is for AES *********')
encVal = encrypt(password)
print('enc result:' + encVal.decode())
print(dycrypt(encVal))
