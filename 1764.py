N, M = input().split()
N = int(N)
M = int(M)
set1 = set()
set2 = set()
for i in range(N):
    word = input()
    set1.add(word)
for i in range(M):
    word = input()
    set2.add(word)
set3 = set1 & set2
li = list(set3)
li.sort()
ListLen = len(li)
print(ListLen)
for i in li:
    print(i)
