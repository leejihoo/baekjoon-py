N = input()
N = int(N)
li = list(map(int, input().split()))
M = input()
M = int(M)
li2 = list(map(int, input().split()))

li3 = []
for i in range(M):
    temp = []
    temp.append(li2[i])
    temp.append(0)
    li3.append(temp)

di = dict(li3)
for i in li:
    if i in di:
        di[i] = di[i] + 1
for val in di.values():
    print(val, end=' ')



