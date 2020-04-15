import math
N = list(map(int,input().split()))
sum = 0
for i in N:
    sum += math.pow(i,2)
sum = sum%10
sum = int(sum)
print(sum)