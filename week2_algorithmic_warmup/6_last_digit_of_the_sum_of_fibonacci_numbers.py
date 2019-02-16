#python3

from math import sqrt,log

fib = lambda n:int((((1+sqrt(5))**n)-((1-sqrt(5))**n))/((2**n)*sqrt(5)))

m = 1
n = int(input())
s = fib(n+2) - fib(m+1)

print(s)
print(927372692193078999175)

print(s%10)
# Failed case #13/17: time limit exceeded
# Input:
# 832564823476

# Your output:

# stderr:
# (Time used: 9.98/5.00, memory used: 9588736/536870912.)
