for index in range(int(input())):
    sudoku = []
    for _ in range(9):
        sudoku.append(list(map(int, input().split())))
        
    check = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = 1
    
    for i in range(9):
        if sorted(sudoku[i]) != check:
            result = 0

    for i in range(9):
        nums = []
        for j in range(9):
            nums.append(sudoku[j][i])
        if sorted(nums) != check:
            result = 0

    for i in range(0, 7, 3):
        for j in range(0, 7, 3):
            nums = []
            for m in range(i, i + 3):
                for n in range(j, j + 3):
                    nums.append(sudoku[m][n])
            if sorted(nums) != check:
                result = 0
    
    print(f'#{index+1} {result}')