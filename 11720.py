N = input()
N =int(N)
Num = input()
Num = int(Num)
sum1 = 0
for i in range(N):
    sum1 = sum1 + Num % 10
    Num = Num // 10
print(sum1)