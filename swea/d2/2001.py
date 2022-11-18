for index in range(int(input())):
    n, m = map(int, input().split())
    board = []
    for i in range(n):
        board.append(list(map(int, input().split())))
    max_sum = 0
    for i in range(n - (m - 1)):
        for j in range(n - (m - 1)):
            sum = 0
            for p in range(m):
                for q in range(m):
                    sum += board[i + p][j + q]
            max_sum = max(max_sum, sum)
    print(f"#{index+1} {max_sum}")
