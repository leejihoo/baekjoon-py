N, M = input().split()
N = int(N)
M = int(M)
listM = list(map(int, input().split()))
MaxSum = 0
for i in range(0, N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum = listM[i] + listM[j] + listM[k]
            if sum <= M:
                if MaxSum < sum:
                    MaxSum = sum
print(MaxSum)
