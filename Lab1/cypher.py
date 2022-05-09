from __future__ import print_function
import Crypto.Cipher.AES as AES
import hashlib
import binascii

# 18051d0908f4cba9 f23d474a3de4d96e 3628a3d8232b7529 5adccca724e8272b

cryptos = ["Bitcoin", "Ethereum", "Tether", "BNB", "XRP", "Terra", "Cardano", "Solana", "Avalanche"]

openssl rsa -in private1.pem -outform PEM -pubout -out public1.pem
openssl rsautl -encrypt -pubin -inkey ./lab4_public.pem -in ./message1 -out ./message_enc


for i in cryptos:
    name = bytes(i)
    rev_name = i[::-1]
    sec = hashlib.sha384((name + b'%s' % i[::-1] + b'2022')).digest()
    cipher = AES.new(sec[:32], AES.MODE_ECB)

    enc_message = b"18051d0908f4cba9f23d474a3de4d96e3628a3d8232b75295adccca724e8272b"
    # decrypt
    # messer = binascii.hexlify(cipher.decrypt(enc_message))
    message = cipher.decrypt(binascii.unhexlify(enc_message))
    print(i)
    print("Encrypted message is %s" % enc_message)
    print("Decrypted message is %s \n" % message)
