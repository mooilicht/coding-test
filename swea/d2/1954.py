for i in range(int(input())):
    print(f"#{i+1}")
    numbers = []
    n = int(input())

    for i in range(n):
        numbers.append([])
        for _ in range(n):
            numbers[i].append(0)

    count = 1

    for index in range(n // 2):
        for i in range(index, n - (index + 1)):
            numbers[index][i] = str(count)
            count += 1
        for i in range(index, n - (index + 1)):
            numbers[i][n - (index + 1)] = str(count)
            count += 1
        for i in reversed(range(index + 1, n - index)):
            numbers[n - (index + 1)][i] = str(count)
            count += 1
        for i in reversed(range(index + 1, n - index)):
            numbers[i][index] = str(count)
            count += 1

    if n % 2 != 0:
        numbers[n // 2][n // 2] = str(count)

    for i in range(n):
        print(" ".join(numbers[i]))
