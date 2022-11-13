board = []
for i in range(19):
    board.append([])
    for j in range(19):
        board[i].append(0)

for i in range(int(input())):
    a, b = map(int, input().split())
    board[a - 1][b - 1] = 1

for i in board:
    for j in i:
        print(j, end=" ")
    print()
