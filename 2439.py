N = input()
N = int(N)
li = []
for i in range(N):
    li.append('*')
    str = ''.join(li)
    print(str.rjust(N))

