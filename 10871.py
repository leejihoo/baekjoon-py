N, M = input().split()
N = int(N)
M = int(M)
li = list(map(int, input().split()))
for i in li:
    if i < M:
        print(i, end=' ')
