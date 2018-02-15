p = (2^31) - 1
q = (2^61) - 1
n = p * q
mString = "HELLOWORLD"
mDecimal = [ord(x) for x in mString]
print list(reversed(mDecimal))
# mDecimal = ZZ(list(reversed(mDecimal)), 100)
