#!/usr/bin/env python
# Demonstrate Arithmetic on secp256k1 curve

E = EllipticCurve(GF(2^256-2^32-977),[0,7])
# Generate a Base Point
E.gens()[0]

P = E.random_point()
# Generate our secret key 
k = 

Q = P*k
print(Q)





