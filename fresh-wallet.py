import base58
import ecdsa
import hashlib
import os

private_key = os.urandom(32).encode("hex")

sk = ecdsa.SigningKey.from_string(private_key.decode("hex"), curve = ecdsa.SECP256k1)

vk = sk.verifying_key

public_key = ('\04' + vk.to_string()).encode("hex")

ripemd160 = hashlib.new('ripemd160')

ripemd160.update(hashlib.sha256(public_key.decode('hex')).digest())

middle_man = '\00' + ripemd160.digest()

checksum = hashlib.sha256(hashlib.sha256(middle_man).digest()).digest()[:4]

binary_addr = middle_man + checksum

addr = base58.b58encode(binary_addr)

print " "
print "Fresh Wallet"
print "============"
print "private key: " + private_key + "\n"
print "public key: " + public_key + "\n"
print "BTC address: " + addr
print " "
