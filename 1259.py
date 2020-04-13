import copy
i = input()
i = int(i)

while i != 0:
    list1 = list(str(i))
    list2 = copy.deepcopy(list1) # 깊은 복사
    list2.reverse()
    judgment = 0
    for j in range(len(list1)):
        if list1[j] != list2[j]:
            print('no')
            judgment = 1
            break
    if judgment == 0:
        print('yes')
    i = input()
    i = int(i)