#𝐵 𝑞 = −(𝑞𝑙𝑜𝑔2𝑞 + (1 − 𝑞) 𝑙𝑜𝑔2(1 − 𝑞) )

import math
import sys

q = sys.argv[1]
if len(q) != 1:
    q1 = int(q[0])
    q2 = int(q[-1])
    q = q1/q2
else: q = int(q)
if q==0: print(0) 
else:
    p = 1 - q
    B = -(q*math.log2(q) + p*math.log2(p))
    print(B)

