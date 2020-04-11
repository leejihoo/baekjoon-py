T = input()
T =int(T)
for i in range(T):
    data = list(map(int,input().split())) # data[0] = H, data[1] = W, data[2] = N
    room = list()                         #  배열[W][H]라고 생각하자
    H = data[0]
    W = data[1]
    N = data[2]
    YY = N % H 
    XX = N // H
    if YY == 0:
        room.append(str(H))
    else:
        room.append(str(YY))

    if (XX+1) < 10:
        room.append('0')

    if YY == 0:
        if(XX == 9):
            room.append('0')
        room.append(str(XX))
    else:
        room.append(str(XX+1))
    print(''.join(room))
