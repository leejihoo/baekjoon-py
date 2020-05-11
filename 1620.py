import sys
N, M = input().split()
li = list()
N = int(N)
M = int(M)
li2 = [[0] * 2 for i in range(N)]
li3 = [[0] * 2 for i in range(N)]
# for i in range(N):
#    str1 = input()
#    li.append(str1)
for i in range(N):
   str1 = sys.stdin.readline().rstrip()
   li2[i][0] = str1
   li2[i][1] = i+1
   li3[i][0] = i + 1
   li3[i][1] = str1
li2 = dict(li2)
li3 = dict(li3)

for i in range(M):
    str1 = sys.stdin.readline().rstrip()
    if str1 in li2:
        print(li2[str1])
    else:
        str1 = int(str1)
        print(li3[str1])
# for i in range(M):
#     str1 = input()
#     str2 = int(ord(str1[0]))
#     if 65 <= str2 <= 90:
#         for j in range(N):
#             if str1 == li[j]:
#                 print(j+1)
#                 break
#     else:
#         str2 = int(str1)
#         print(li[str2-1])




