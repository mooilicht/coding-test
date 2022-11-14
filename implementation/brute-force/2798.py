n, m = map(int, input().split())
numbers = list(map(int, input().split()))
max_nums = []
for i in range(len(numbers) - 2):
    for j in range(i + 1, len(numbers) - 1):
        for k in range(j + 1, len(numbers)):
            sum = numbers[i] + numbers[j] + numbers[k]
            if m >= sum:
                max_nums.append(sum)
print(max(max_nums))
