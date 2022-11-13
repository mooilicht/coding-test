result = []
for i in range(23):
    result.append(0)

n = int(input())
random_list = map(int, input().split())

for i in random_list:
    result[i - 1] += 1

for i in result:
    print(i, end=" ")
