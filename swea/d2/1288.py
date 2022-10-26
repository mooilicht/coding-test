for k in range(int(input())):
    n = int(input())
    m = 0
    checks = [False, False, False, False, False, False, False, False, False, False]
    while True:
        if False in checks:
            m += 1
            nums = list(str(n * m))
            for i in nums:
                checks[int(i)] = True
        else:
            print(f"#{k+1} {n * m}")
            break
