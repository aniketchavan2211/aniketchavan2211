#!/usr/bin/env python3
import rsa

# creating new public and private keys
public_key, private_key = rsa.newkeys(1024)

# exporting public and private keys
with open("public.pem", "rb") as f:
  # f.write(public_key.save_pkcs1("PEM"))
  public_key = rsa.PublicKey.load_pkcs1(f.read())

with open("private.pem", "rb") as f:
  # f.write(private_key.save_pkcs1("PEM"))
  private_key = rsa.PrivateKey.load_pkcs1(f.read())

msg = "Hello" # message

## Encrypting message
# encrypted_msg = rsa.encrypt(msg.encode(), public_key)
# print(encrypted_msg)

## Exporting encrypted message
# with open("encrypted_msg", "wb") as f:
#    f.write(encrypted_msg)

## Decrypting message
# encrypted_msg = open("encrypted_msg", "rb").read() # opening encrypted message
# clear_message = rsa.decrypt(encrypted_msg, private_key)
# print(clear_message.decode())

## Digital Signatures (checks integrity)
# signature = rsa.sign(msg.encode(), private_key, "SHA-256") # signing message with private key

with open("signature", "rb") as f: # make changes wb > rb if already signature exists
  # f.write(signature)
  signature = f.read() # reading sugnature file

## Verifying
print(rsa.verify(msg.encode(), signature, public_key)) # if prints SHA-256 then it auenticated/verified
