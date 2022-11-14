while True:
    n = input()
    if n == "0":
        break
    words = list(n)
    re_words = words[::-1]
    if words == re_words:
        print("yes")
    else:
        print("no")
