N, M = input().split()
N = int(N)
M = int(M)
if M-45 < 0:
    if N-1 < 0:
        N = 23
    else:
        N = N - 1
    M = M + 15
else:
    M = M - 45
print(N, M)
