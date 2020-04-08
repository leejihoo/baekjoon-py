sound = list(map(str,input().split()))
asc = "12345678"
des = "87654321"
soundJoin = ''.join(sound)
if soundJoin == asc:
    print("ascending")
elif soundJoin == des:
    print("descending")
else:
    print("mixed")
