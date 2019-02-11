#python3
fib_list = [0,1]

n_fib = int(input())
for x in range(n_fib):
    elem = fib_list[-1]+fib_list[-2]
    fib_list.append(elem)

print(fib_list[-2])