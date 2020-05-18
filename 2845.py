N, M = input().split()
N = int(N)
M = int(M)
li = list(map(int, input().split()))
sum = N * M
for i in range(len(li)):
    li[i] = li[i] - sum
for i in li:
    print(i, end=" ")
