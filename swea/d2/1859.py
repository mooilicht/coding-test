T = int(input())
for index in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    numbers.reverse()
    max_num = 0
    profit = 0
    for i in numbers:
        if i >= max_num:
            max_num = i
        else:
            profit += max_num - i
    print(f"#{index} {profit}")
