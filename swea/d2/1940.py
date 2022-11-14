for i in range(int(input())):
    result = 0
    current = 0
    for j in range(int(input())):
        commands = list(map(int, input().split()))
        if commands[0] == 0:
            result += current
        elif commands[0] == 1:
            current += commands[1]
            result += current
        else:
            if commands[1] > current:
                current = 0
            else:
                current -= commands[1]
                result += current
    print(f"#{i+1} {result}")
