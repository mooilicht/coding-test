for i in range(int(input())):
    n = input()
    numbers = list(map(int, input().split()))
    numbers.sort()
    strs = list(map(str, numbers))
    print(f"#{i+1} {' '.join(strs)}")
