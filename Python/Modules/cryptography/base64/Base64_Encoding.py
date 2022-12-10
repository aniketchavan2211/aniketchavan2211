#!/usr/bin/env python3

# Encoding data & Decoding data
import base64

# 'Hello' is a plain text
msg = b'Hello' # b is for bytes format
print("This is message: ", msg)

# Encoding 'Hello'
encoded_msg = base64.b64encode(msg)
print("Encoded data: ", encoded_msg)

# Decoding 'encoded_msg'
decoded_msg = base64.b64decode(encoded_msg)
print("Decoded data: ", decoded_msg)
