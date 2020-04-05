while(True):
    A,B = input().split()
    A = int(A)
    B = int(B)
    C = A + B
    if 0<A and A<10 and 0<B and B<10:
        print(C)
    if A == 0 and B == 0:
        break

