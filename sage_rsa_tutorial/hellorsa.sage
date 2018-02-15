p = (2^31) - 1
q = (2^61) - 1
n = p * q
mString = "HELLOWORLD"
mDecimal = [ord(x) for x in mString]

'''
The 100 tells you how much to multiply each element of the list by, in powers. Think of it as "base 100".

sage: ZZ([1,2,3],100)
30201
sage: ZZ([1,2,3],2)
17
sage: ZZ([1,2,3],10) # 1*10^0+2*10^1+3*10^2
321
'''

mDecimal = ZZ(list(reversed(mDecimal)), 100)
print("Message: " + mString) 
print("Message in decimal: " + str(mDecimal))

if is_prime(p):
    print("p: " + str(p))

if is_prime(q):
    print("q: " + str(q))

print("n: " + str(n))

# get phi
phi = (p-1)*(q-1)
print("phi: " + str(phi))

# find e where it has a common denominator with phi of 1
# and e is less than n. e will also be random
e = ZZ.random_element(phi)
while (gcd(e, phi) != 1) and (e < n):
    e = ZZ.random_element(phi)

print("e: " + str(e))

# find d
# de - k * phi(n) = 1 
# de = 1 ( mod( phi(n) ) )
# Bezout identity : g = gcd(x,y) = sx + ty
# bezout will be random as well

bezout = xgcd(e, phi)
print("bezout: " + str(bezout))

d = Integer(mod(bezout[1], phi))
print("d: " + str(d))

# mod(d * e, phi) must equal 1
print("mod(d*e,phi): " + str(mod(d*e,phi)))

print("public key (n,e): (" + str(n) + "," + str(e) + ")")
print("private key (p,q,d): (" + str(p) + "," + str(q) + "," + str(d) + ")" )

# encrypt message
c = power_mod(mDecimal, e, n)
print("c: " + str(c))


# decrypt message
mDecrypt = power_mod(c, d, n)
print("mDecrypt: " + str(mDecrypt))


# Decimal to string
dMessage = ''.join([chr(int(str(mDecrypt)[i:i+2])) for i in range (0, len(str(mDecrypt)), 2)])
eMessage = ''.join([chr(int(str(c)[i:i+2])) for i in range (0, len(str(c)), 2)])

print("Encrypted Message: " + eMessage)
print("Decrypted Message: " + dMessage)
