#python3

from math import sqrt,log

def fib(n):
    v1, v2, v3 = 1, 1, 0    # initialise a matrix [[1,1],[1,0]]
    for rec in bin(n)[3:]:  # perform fast exponentiation of the matrix (quickly raise it to the nth power)
        calc = v2*v2
        v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
        if rec=='1':    v1, v2, v3 = v1+v2, v1, v2
    return v2

a = input().split()
n,m = int(a[0]),int(a[1])
f = fib(n)

print(f)
print(39679027332006820581608740953902289877834488152161)
print(f%m)