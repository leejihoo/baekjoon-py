def mergeSort(x, y):
    if len(x) > 1:
        mid = len(x)//2
        lx, rx = x[:mid], x[mid:]
        ly, ry = y[:mid], y[mid:]
        mergeSort(lx, ly)
        mergeSort(rx, ry)

        li, ri, i = 0, 0, 0
        while li < len(lx) and ri < len(rx):
            if lx[li] < rx[ri]:
                x[i] = lx[li]
                y[i] = ly[li]
                li += 1
            elif lx[li] > rx[ri]:
                x[i] = rx[ri]
                y[i] = ry[ri]
                ri += 1
            else:
                if ly[li] < ry[ri]:
                    x[i] = lx[li]
                    y[i] = ly[li]
                    li += 1
                else:
                    x[i] = rx[ri]
                    y[i] = ry[ri]
                    ri += 1
            i += 1
        x[i:] = lx[li:] if li != len(lx) else rx[ri:]
        y[i:] = ly[li:] if li != len(ly) else ry[ri:]

N = input()
N = int(N)
liX = list()
liY = list()
for i in range(N):
    A, B = input().split()
    A = int(A)
    B = int(B)
    liX.append(A)
    liY.append(B)
#
# for i in range(0, N):
#     for j in range(0, N-i-1):
#         if liX[j] > liX[j+1]:
#             tempX = liX[j]
#             tempY = liY[j]
#             liX[j] = liX[j+1]
#             liY[j] = liY[j+1]
#             liX[j+1] = tempX
#             liY[j+1] = tempY
#         elif liX[j] == liX[j+1]:
#             if liY[j] > liY[j + 1]:
#                 tempX = liX[j]
#                 tempY = liY[j]
#                 liX[j] = liX[j + 1]
#                 liY[j] = liY[j + 1]
#                 liX[j + 1] = tempX
#                 liY[j + 1] = tempY
mergeSort(liX, liY)

for i in range(N):
    print(liX[i], liY[i])
