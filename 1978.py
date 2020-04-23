N = input()
N = int(N)
li = list(map(int,input().split()))
dec = 0 #소수의 갯수
for i in li:
    count = 0
    for j in range(2, i+1): #2부터 자기자신까지 1은 소수가 아니다
        if i % j == 0:
            count = count + 1
    if count == 1:
        dec = dec + 1
print(dec)
