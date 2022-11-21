for i in range(int(input())):
    hour1, minute1, hour2, minute2 = map(int, input().split())
    hour = hour1 + hour2
    minute = minute1 + minute2
    if minute >= 60:
        minute -= 60
        hour += 1
    if hour >= 12:
        hour -= 12
    print(f"#{i+1} {hour} {minute}")
