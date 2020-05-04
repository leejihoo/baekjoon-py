def LowerBound(key, list1):
    len1 = len(list1)
    low = 0
    high = len1
    while low < high:
        mid = (low+high)//2
        if key > list1[mid]:
            low = mid + 1
        else:
            high = mid
    return high + 1

def UpperBound(key, list1):
    len1 = len(list1)
    low = 0
    high = len1
    while low < high:
        mid = (low+high)//2
        if key >= list1[mid]:
            low = mid + 1
        else:
            high = mid
    return high + 1

if __name__ == "__main__":
    N = input()
    N = int(N)
    li1 = list(map(int, input().split()))
    set1 = set(li1)
    M = input()
    M = int(M)
    li2 = list(map(int, input().split()))
    li1.sort()
    for i in li2:
        Low = LowerBound(i, li1)
        Up = UpperBound(i, li1)
        print(Up-Low, end=" ")

