#python3
def gcd(a,b):
    i = 0
    while True:
        if b == 0:
            return a
        else:
            a_pr = a%b
            a = b
            b = a_pr

a,b = input().split()
a,b = int(a),int(b)
gcd = gcd(a,b)
print(gcd)
#Good job! (Max time used: 0.03/5.00, max memory used: 9900032/536870912.)