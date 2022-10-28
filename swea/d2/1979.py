for m in range(int(input())):
    puzzle = []
    n, k = map(int, input().split())
    for p in range(n):
        puzzle.append(list(map(int, input().split())))
    result = 0
    for i in range(n):
        count = 0
        for j in range(n):
            if puzzle[i][j] == 1:
                count += 1
            if puzzle[i][j] == 0 or j == n - 1:
                if count == k:
                    result += 1
                count = 0
        count = 0
        for j in range(n):
            if puzzle[j][i] == 1:
                count += 1
            if puzzle[j][i] == 0 or j == n - 1:
                if count == k:
                    result += 1
                count = 0
    print(f"#{m+1} {result}")
