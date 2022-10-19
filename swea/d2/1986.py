for i in range(int(input())):
    num = int(input())
    sum = 0
    for n in range(1, num + 1):
        if n % 2 == 0:
            sum -= n
        else:
            sum += n
    print(f"#{i+1} {sum}")
