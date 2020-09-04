# words = "AAAA"
# hex = "".join([hex(ord(x)) for x in words]).replace("0x", "")
# i = int(hex,16)
# print(i)
#


words = "AAAA"

for x in words:
    hex1 = hex(ord(x)).replace("0x", "")
    i = int(hex1, 16)
    print(i)