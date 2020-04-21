N = input()
N = int(N)
li = list(map(int,input().split()))
d = dict()
for i in range(N):
    d[li[i]] = li[i]

M = input()
M = int(M)
li2 = list(map(int,input().split()))

for i in range(M):
    if li2[i] in d:
        print(1)
    else:
        print(0)
# for i in range(M):
#     for j in range(N):
#         if li2[i] == li[j]:
#           print("1")
#           break
#         else:
#             if j == N-1:
#                 print("0")


