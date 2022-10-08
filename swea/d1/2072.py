for i in range(int(input())):
    numbers = list(map(int, input().split()))
    sum = 0
    for num in numbers:
        if num % 2 != 0:
            sum += num
    print(f"#{i+1} {sum}")
