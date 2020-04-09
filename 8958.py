N = input()
N = int(N)
for i in range(N):
    quiz = input()
    length = len(quiz)
    sum = 0 # 총 점수
    N = 0 # 각 문제의 점수
    for j in range(length):
        if quiz[j] == 'O':
            if j == 0:
                N = 1
                sum = sum + N

            elif quiz[j-1] == 'O':
                N+=1
                sum = sum + N

            elif quiz[j - 1] == 'X' and quiz[j] == 'O':
                N = 1
                sum = sum + N

        else:
            N = 0
    print(sum)