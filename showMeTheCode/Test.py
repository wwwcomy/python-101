from openpyxl import load_workbook
import xml.etree.ElementTree as ET
import os
import sys
import binascii

def createSalt(salt=None):
    if salt is None:
        salt = os.urandom(8) # 64 bits.
    print(salt)
    print(type(salt))
    sSalt = str(salt)
    print(sSalt)
    print(type(sSalt))

    revertSalt = eval(sSalt)
    print(revertSalt)
    print(type(revertSalt))

    hexlifiedSalt = binascii.hexlify(salt)
    print (hexlifiedSalt)
    print (hexlifiedSalt.decode())

    unhexlifiedSalt = binascii.unhexlify(hexlifiedSalt)
    print (unhexlifiedSalt)


createSalt("123")