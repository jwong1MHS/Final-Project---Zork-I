import os,binascii

print (binascii.b2a_hex(os.urandom(15)))
#used for generating random 30 digit hex string