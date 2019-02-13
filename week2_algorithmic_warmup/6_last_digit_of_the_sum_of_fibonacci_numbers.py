#python3

n_fib = int(input())

n,m = 0,1
s = 0
for x in range(n_fib):
    s += m
    n,m = m%10,n%10+m%10

print(s%10)