import base64
hexadecimal_str = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'
hex_ee = bytes.fromhex(hexadecimal_str)
print (base64.b64encode(hex_ee))