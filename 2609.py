def GCD (n,m):
    if n < m:
        tmp = n
        n = m
        m = tmp

    if n % m == 0:
        return m
    elif n % m != 0:
        return GCD(m, n%m)

def LCM (n, m):
    gcd = GCD(n, m)
    return n*m//gcd

n, m = input().split()
n = int(n)
m = int(m)
print(GCD(n, m))
print(LCM(n, m))
