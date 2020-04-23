import collections
N = input()
N = int(N)
qu = collections.deque()
for i in range(1,N+1):
    qu.append(i)
for i in range(N-1):
    qu.popleft()
    Two = qu.popleft()
    qu.append(Two)
print(qu[0])
# li = list()
# for i in range(1,N+1):
#     li.append(N+1-i)
# for i in range(N-1):
#     li.pop()
#     two = li.pop()
#     li.insert(0, two)
# print(li[0])



