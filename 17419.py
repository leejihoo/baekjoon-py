# N = int(input())
# b = '0b'
# Bit = input()
# Bit = int(b + Bit, 2)
# count = 1
# while not (Bit == (Bit & ((~Bit)+1))):
#     Bit = Bit - (Bit & ((~Bit) + 1))
#     count = count + 1
# print(count)
N = int(input())
Bit = input()
count = 0
for i in Bit:
    if i == '1':
        count = count + 1
print(count)