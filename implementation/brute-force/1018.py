n, m = map(int, input().split())
board = []
for i in range(n):
    colors = list(input())
    board.append(colors)
result = 64
for i in range(n - 7):
    for j in range(m - 7):
        count_b = 0
        count_w = 0
        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if a % 2 == 0:
                    if b % 2 == 0:
                        if board[a][b] != "B":
                            count_b += 1
                        else:
                            count_w += 1
                    else:
                        if board[a][b] != "W":
                            count_b += 1
                        else:
                            count_w += 1
                else:
                    if b % 2 == 0:
                        if board[a][b] != "W":
                            count_b += 1
                        else:
                            count_w += 1
                    else:
                        if board[a][b] != "B":
                            count_b += 1
                        else:
                            count_w += 1
        result = min(result, min(count_b, count_w))
print(result)
