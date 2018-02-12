#!/usr/bin/python

import gmpy2

p = 863653476616376575308866344984576466644942572246900013156919
q = 965445304326998194798282228842484732438457170595999523426901
e = 65537
d = gmpy2.invert(e, (p - 1) * (q - 1))

print '''asn1=SEQUENCE:rsa_key

[rsa_key]
version=INTEGER:0
modulus=INTEGER:{n}
pubExp=INTEGER:{e}
privExp=INTEGER:{e1}
p=INTEGER:{p}
q=INTEGER:{q}
e1=INTEGER:{e1}
e2=INTEGER:{e2}
coeff=INTEGER:{coeff}'''.format(
    n=p * q,
    e=e,
    p=p,
    q=q,
    e1=d % (p - 1),
    e2=d % (q - 1),
    coeff=gmpy2.invert(q, p),
)
