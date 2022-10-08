for i in range(int(input())):
    date = input()
    year = date[:4]
    month = date[4:6]
    day = date[6:]
    result = ""
    if 1 <= int(month) <= 12:
        if month == "02" and 1 <= int(day) <= 28:
            result = f"{year}/{month}/{day}"
        elif month in ["04", "06", "09", "11"] and 1 <= int(day) <= 30:
            result = f"{year}/{month}/{day}"
        elif (
            month in ["01", "03", "05", "07", "08", "10", "12"] and 1 <= int(day) <= 31
        ):
            result = f"{year}/{month}/{day}"
        else:
            result = -1
    else:
        result = -1
    print(f"#{i+1} {result}")
