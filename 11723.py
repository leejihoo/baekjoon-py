import sys
input1 = sys.stdin.readline


# def binary_search(li, val):
# #     low = 0
# #     high = len(li) - 1
# #     while low <= high:
# #         mid = (low + high) // 2
# #         if li[mid] < val:
# #             low = mid + 1
# #         elif li[mid] > val:
# #             high = mid - 1
# #         else:
# #             return True
# #     return False


N = input()
N = int(N)
li1 = [False for i in range(21)]
for i in range(N):
    word = input1().split()
    if word[0] == "add":
        # if word[1] not in li1:
        # if not binary_search(li1, word[1]):
        #     li1.append(word[1])
            word1 = int(word[1])
            li1[word1] = True
    elif word[0] == "remove":
        # if word[1] in li1:
        # if binary_search(li1, word[1]):
        #     li1.remove(word[1])
            word1 = int(word[1])
            li1[word1] = False
    elif word[0] == "check":
        word1 = int(word[1])
        if li1[word1] == True:
        # if binary_search(li1, word[1]):
            print("1")
        else:
            print("0")
    elif word[0] == "toggle":
        word1 = int(word[1])
        li1[word1] = not li1[word1]
        # if binary_search(li1, word[1]):
        #     li1[word1] = False
        # else:
        #     li1[word1] = True
    elif word[0] == "all":
        # while len(li1) > 0:
        #     del li1[0]
        for j in range(21):
            li1[j] = True
    elif word[0] == "empty":
        for j in range(21):
            li1[j] = False
        # while len(li1) > 0:
        #     del li1[0]
