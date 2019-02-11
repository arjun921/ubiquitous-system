# python3

from math import gcd

def lcm(a,b):
    lcm_ = (a*b)/gcd(a,b)
    print(lcm_)
    return int(lcm_)

a,b = input().split()
a,b = int(a),int(b)
lcm_ = lcm(a,b)
print(lcm_)