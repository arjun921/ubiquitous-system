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
lcm_ = lcm(a,b)

print(lcm_)
#Good job! (Max time used: 0.05/5.00, max memory used: 9932800/536870912.)
