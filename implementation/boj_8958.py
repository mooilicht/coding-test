for i in range(int(input())):
    answers = list(input())
    result = 0
    count = 0
    for i in answers:
        if i == "O":
            count += 1
            result += count
        else:
            count = 0
    print(result)
