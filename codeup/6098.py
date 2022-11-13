board = []
for i in range(10):
    board_list = list(map(int, input().split()))
    board.append(board_list)

x, y = 1, 1
board[x][y] = 9

while True:
    if board[x][y] == 2:
        board[x][y] = 9
        break
    elif x == 9 or y == 9:
        break
    else:
        board[x][y] = 9

    if board[x][y + 1] == 0 or board[x][y + 1] == 2:
        y += 1
    else:
        x += 1

for i in board:
    for j in i:
        print(j, end=" ")
    print()
