for i in range(int(input())):
    m1, d1, m2, d2 = map(int, input().split())
    sum = 0
    if m1 == m2:
        sum += d2 - d1 + 1
    else:
        for j in range(m1, m2 + 1):
            if j in [1, 3, 5, 7, 8, 10, 12]:
                sum += 31
            elif j in [4, 6, 9, 11]:
                sum += 30
            else:
                sum += 28
        sum -= d1
        if m2 in [1, 3, 5, 7, 8, 10, 12]:
            sum -= 31
            sum += d2 + 1
        elif m2 in [4, 6, 9, 11]:
            sum -= 30
            sum += d2 + 1
        else:
            sum -= 28
            sum += d2 + 1
    print(f"#{i+1} {sum}")
