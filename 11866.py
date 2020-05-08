N, K = input().split()
N = int(N)
K = int(K)
li1 = list()
li2 = list()
count = K - 1
for i in range(1, N+1):
    li1.append(i)
for i in range(0, N):
    if i > 0:
        count = count + K - 1
    if count >= len(li1):
        count = count % len(li1)
        li2.append(li1[count])
        del li1[count]
    else:
        li2.append(li1[count])
        del li1[count]
print("<", end="")
for i in range(N):
    if i != N-1:
        print(li2[i], end=", ")
    else:
        print(li2[i], end="")
print(">", end="")