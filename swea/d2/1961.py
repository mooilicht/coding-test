for k in range(int(input())):
    n = int(input())
    numbers = []
    for num in range(n):
        numbers.append(input().split())
    first = []
    second = []
    third = []

    for i in range(n):
        word = ""
        for j in reversed(range(n)):
            word += numbers[j][i]
        first.append(word)

    for i in reversed(range(n)):
        word = ""
        for j in reversed(range(n)):
            word += numbers[i][j]
        second.append(word)

    for i in reversed(range(n)):
        word = ""
        for j in range(n):
            word += numbers[j][i]
        third.append(word)

    print(f"#{k + 1}")
    for i in range(n):
        print(first[i], second[i], third[i])
