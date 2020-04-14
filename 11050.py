import math
N, K = input().split()
N = int(N)
K = int(K)
mol = math.factorial(N)  # 분자
de = math.factorial(K) * math.factorial(N-K)  # 분모
R = mol//de
print(R)

