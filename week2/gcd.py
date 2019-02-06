def gcd(a,b):
    i = 0
    while True:
        print(i)
        if b == 0:
            return a
        else:
            a_pr = a%b
            a = b
            b = a_pr
