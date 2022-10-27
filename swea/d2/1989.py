for i in range(int(input())):
    words = list(input())
    re_words = words[::-1]
    a = 0
    if words == re_words:
        a = 1
    print(f"#{i+1} {a}")
