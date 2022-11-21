for index in range(int(input())):
    print(f"#{index+1}")
    result = []
    for i in range(int(input())):
        line = []
        for j in range(i + 1):
            if j == 0 or j == i:
                line.append(1)
            else:
                line.append(result[i - 1][j - 1] + result[i - 1][j])
        result.append(line)
    for i in result:
        print(" ".join(list(map(str, i))))
