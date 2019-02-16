# python3

import decimal

def gcd(a,b):
    while True:
        if b == 0:
            return a
        else:
            a_pr = a%b
            a = b
            b = a_pr

def lcm(a,b):
    gcd_ = gcd(a,b)
    # python rounds off decimals beyond certain number hence outputs were varying from expected
    # using decimal to ensure accuracy.
    a,b = decimal.Decimal(a),decimal.Decimal(b)
    lcm_ = (a*b)/gcd_
    return int(lcm_)

a,b = input().split()
a,b = int(a),int(b)
# a,b = 226553150,1023473145
lcm_ = lcm(a,b)

print(lcm_)