# import sys
# input1 = sys.stdin.readline
#
#
# # def binary_search(li, val):
# # #     low = 0
# # #     high = len(li) - 1
# # #     while low <= high:
# # #         mid = (low + high) // 2
# # #         if li[mid] < val:
# # #             low = mid + 1
# # #         elif li[mid] > val:
# # #             high = mid - 1
# # #         else:
# # #             return True
# # #     return False
#
#
# N = input()
# N = int(N)
# li1 = []
# for i in range(N):
#     word = input1().split()
#     if word[0] == "add":
#         if word[1] not in li1:
#         # if not binary_search(li1, word[1]):
#             li1.append(word[1])
#     elif word[0] == "remove":
#         if word[1] in li1:
#         # if binary_search(li1, word[1]):
#             li1.remove(word[1])
#     elif word[0] == "check":
#         if word[1] in li1:
#         # if binary_search(li1, word[1]):
#             print("1")
#         else:
#             print("0")
#     elif word[0] == "toggle":
#         if word[1] in li1:
#         # if binary_search(li1, word[1]):
#             li1.remove(word[1])
#         else:
#             li1.append(word[1])
#     elif word[0] == "all":
#         li1.clear()
#         # while len(li1) > 0:
#         #     del li1[0]
#         for j in range(20):
#             li1.append(str(j+1))
#     elif word[0] == "empty":
#         li1.clear()
#         # while len(li1) > 0:
#         #     del li1[0]
import sys

resultSet = 0
executeCount = sys.stdin.readline()

for i in range(0, int(executeCount)):
    operatorStr = sys.stdin.readline()
    executeOperator = operatorStr.split(" ")[0]
    executeNumber = 0

    if executeOperator != "all\n" and executeOperator != "empty\n":
        executeNumber = int(operatorStr.split(" ")[1]) - 1

    if executeOperator == "add":
        resultSet |= (1 << executeNumber)
    elif executeOperator == "remove":
        resultSet &= ~(1 << executeNumber)
    elif executeOperator == "check":
        if resultSet & (1 << executeNumber):
            print("1")
        else:
            print("0")
    elif executeOperator == "toggle":
        if resultSet & (1 << executeNumber):
            resultSet = (resultSet & ~(1 << executeNumber))
        else:
            resultSet |= (1 << executeNumber)
    elif executeOperator == "all\n":
        resultSet = (1 << 20) - 1
    elif executeOperator == "empty\n":
        resultSet &= 0

