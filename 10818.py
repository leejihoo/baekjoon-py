N = int(input())
list1 = list(map(int, input().split())) #map함수를 사용하여 한줄에 여러개의 변수를 입력받음
list1.sort()
print(list1[0] , list1.pop())