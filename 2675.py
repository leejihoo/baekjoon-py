N = input()
N = int(N)
Re = 0
for i in range(0,N):
    list1 = list()
    Re, list1 = input().split()
    Re = int(Re)
    for j in range(0, len(list1)):

        for k in range(0, Re):
            print(list1[j], end='')
    print()

