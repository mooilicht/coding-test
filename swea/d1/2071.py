for i in range(int(input())):
    numbers = map(int, input().split())
    print(f"#{i+1} {round(sum(numbers)/10)}")
