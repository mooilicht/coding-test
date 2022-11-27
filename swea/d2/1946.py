for index in range(1, int(input()) + 1):
    print(f"#{index}")
    text = ""
    for _ in range(int(input())):
        c, k = input().split()
        k = int(k)
        text += c * k
    for i in range(len(text)):
        print(text[i], end="")
        if (i + 1) % 10 == 0:
            print()
    print()
