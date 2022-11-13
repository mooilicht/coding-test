h, w = map(int, input().split())
board = []
for i in range(h):
    board.append([])
    for j in range(w):
        board[i].append(0)

for i in range(int(input())):
    l, d, x, y = map(int, input().split())

    if d == 0:
        for j in range(y - 1, y + l - 1):
            board[x - 1][j] = 1
    else:
        for j in range(x - 1, x + l - 1):
            board[j][y - 1] = 1

for i in board:
    for j in i:
        print(j, end=" ")
    print()
