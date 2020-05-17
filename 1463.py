N = int(input())
index = 0
minVal = 0
li = list()
li.append(0)
li.append(0)
li.append(1)
li.append(1)
for i in range(4, 1000001):
    i3 = 0
    i2 = 0
    i1 = 0
    if i % 3 == 0:
        i3 = i // 3
    if i % 2 == 0:
        i2 = i // 2
    i1 = i - 1
    if i % 6 == 0:
        minVal = min(li[i1], li[i2], li[i3])
    elif i % 3 == 0 and i % 2 != 0:
        minVal = min(li[i1],  li[i3])
    elif i % 3 != 0 and i % 2 == 0:
        minVal = min(li[i1], li[i2])
    else:
        minVal = li[i1]

    if minVal == li[i1]:
        index = i1
    elif minVal == li[i2]:
        index = i2
    else:
        index = i3
    li.append(li[index] + 1)
# while N != 1:
#     if N % 3 == 0:
#         N = N // 3
#     elif N % 2 == 0:
#         N = N // 2
#     else:
#         N = N - 1
#     count = count + 1
print(li[N])

