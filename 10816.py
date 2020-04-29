def binary_search(key, list1):
    len1 = len(list1)
    list1 = list(list1)
    low = 0
    high = len1-1
    while low < high:
        mid = (low+high)//2
        if key > list1[mid]:
            low = mid + 1
        elif key < list1[mid]:
            high = mid - 1
        else:
            return mid
    return -1

if __name__ == "__main__":
    N = input()
    N = int(N)
    li1 = list(map(int, input().split()))
    set1 = set(li1)
    M = input()
    M = int(M)
    li2 = list(map(int, input().split()))
    di = dict()
    li3 = [0 for i in range(len(set1))]
    for i in li1:
        if binary_search(i, set1) > 0:
            li3[binary_search(i, set1)] = li3[binary_search(i, set1)] + 1
    for i in li2:
        print(li3[binary_search(i, set1)], end='')

