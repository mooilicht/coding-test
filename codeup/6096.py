board = []
for i in range(19):
    dol_list = list(map(int, input().split()))
    board.append(dol_list)

for i in range(int(input())):
    a, b = map(int, input().split())
    for x in range(19):
        if board[x][b - 1] == 1:
            board[x][b - 1] = 0
        else:
            board[x][b - 1] = 1
    for y in range(19):
        if board[a - 1][y] == 1:
            board[a - 1][y] = 0
        else:
            board[a - 1][y] = 1

for i in board:
    for j in i:
        print(j, end=" ")
    print()
