import sys
input = sys.stdin.readline
N = input().strip()
N = int(N)
stack = list()
for i in range(N):
    li = input().split()
    if li[0] == "push_front":
        StLen = len(stack)
        StLen = int(StLen)
        stack.insert(0, li[1])
    if li[0] == "push_back":
        StLen = len(stack)
        StLen = int(StLen)
        stack.append(li[1])
    elif li[0] == "pop_front":
        StLen = len(stack)
        StLen = int(StLen)
        if StLen > 0:
            print(stack[0])
            del stack[0]
        else:
            print("-1")
    elif li[0] == "pop_back":
        StLen = len(stack)
        StLen = int(StLen)
        if StLen > 0:
            print(stack[StLen-1])
            del stack[StLen-1]
        else:
            print("-1")
    elif li[0] == "size":
        StLen = len(stack)
        StLen = int(StLen)
        print(StLen)
    elif li[0] == "empty":
        StLen = len(stack)
        StLen = int(StLen)
        if StLen > 0:
            print("0")
        else:
            print("1")
    elif li[0] == "front":
        StLen = len(stack)
        StLen = int(StLen)
        if StLen > 0:
            print(stack[0])
        else:
            print("-1")
    elif li[0] == "back":
        StLen = len(stack)
        StLen = int(StLen)
        if StLen > 0:
            print(stack[StLen - 1])
        else:
            print("-1")


