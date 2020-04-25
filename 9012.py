N = input()
N = int(N)
for i in range(N):
    count = 0;
    li = input()
    for j in li:
        if j == '(':
           count = count + 1
        elif j == ')':
            count = count - 1
        if count < 0:
            break
    if count == 0:
        print("YES")
    else:
        print("NO")

