import os,binascii

print (binascii.b2a_hex(os.urandom(15)))
#used for generating random 30 digit hex string
#https://stackoverflow.com/questions/2782229/most-lightweight-way-to-create-a-random-string-and-a-random-hexadecimal-number
