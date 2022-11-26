result = ""
for i in range(1, int(input()) + 1):
    count = 0
    for word in str(i):
        if word == "3" or word == "6" or word == "9":
            count += 1
    if count == 0:
        result += str(i)
    else:
        result += count * "-"
    result += " "
print(result.strip())
