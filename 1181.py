N = input()
N = int(N)
word = list()
for i in range(N):
    word.append(input())
word.sort(key=len)
word = set(word)  # 중복 제거
wordLen = [[] for i in range(55)]
for i in word:
    wordLen[len(i)].append(i)
for i in wordLen:
    i.sort()
for i in range(55):
    for j in wordLen[i]:
        print(j)
