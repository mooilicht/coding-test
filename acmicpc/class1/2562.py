# https://www.acmicpc.net/problem/2562
list = []
for i in range(9):
    list.append(int(input()))

result = max(list)
print(result)
print(list.index(result) + 1)
