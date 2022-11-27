for index in range(1, int(input()) + 1):
    numbers = list(map(int, input().split()))
    numbers.remove(min(numbers))
    numbers.remove(max(numbers))
    print(f"#{index} {round(sum(numbers) / len(numbers))}")
