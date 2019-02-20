#python3

# """
# Greedy Algorithm 1
# denominations <= [10,5,1]

# m = 2
# coins = 0
# while m!= 0
#     change = denominations[0]
#     if change>m
#         remove change from (denominations)
#         break
#     if change<m
#         coins +=1
#         m = m-change

# """

denominations = [10,5,1]

m = int(input())
coins_needed = 0

while m!=0:
    change = denominations[0]
    if change>m:
        denominations.remove(change)
    if change<=m:
        coins_needed +=1
        m = m - change

print(coins_needed)

# Good job! (Max time used: 0.03/5.00, max memory used: 9609216/536870912.)
