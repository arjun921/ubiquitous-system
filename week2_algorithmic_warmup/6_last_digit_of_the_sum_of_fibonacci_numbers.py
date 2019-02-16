#python3

from math import sqrt,log

fib = lambda n:int((((1+sqrt(5))**n)-((1-sqrt(5))**n))/((2**n)*sqrt(5)))

m = 1
n = int(input())
s = fib(n+2) - fib(m+1)

print(s)
print(927372692193078999175)

print(s%10)