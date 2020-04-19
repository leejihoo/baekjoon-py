N = input()
N = int(N)
li = [[] for i in range(201)]
for i in range(N):
    a, b = input().split()
    a = int(a)
    li[a].append(b)
for i in range(201):
    for j in li[i]:
        print(i, j)

