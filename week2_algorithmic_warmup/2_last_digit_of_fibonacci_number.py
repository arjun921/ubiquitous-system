#python3

n_fib = int(input())-1

n,m = 0,1
for x in range(n_fib):
    n,m = m%10,n%10+m%10

print(m)