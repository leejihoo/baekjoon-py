A = input()
B = input()
C = input()
A = int(A)
B = int(B)
C = int(C)
prod = A * B * C
li = [0 for i in range(10)]
while prod > 0:
    re = prod % 10
    re = int(re)
    li[re] = li[re] + 1
    prod = prod // 10
for i in li:
    print(i)

