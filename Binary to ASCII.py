import binascii
inp = (input("Enter a binary number"))
inp = bytes(inp.encode('utf-8'))
dataConv = binascii.b2a_uu(inp)
print(dataConv)

