import copy
list1 = list()
order = 0
for i in range(0,9):
    N = input()
    N = int(N)
    list1.append(N)
list2 = copy.deepcopy(list1)
list1.sort()
MAX = list1.pop()

for i in range(0,9):
    if MAX == list2[i]:
        order = i+1
        break

print(MAX)
print(order)