def days2(year, month):
    leafYear = False
    dal = {1, 3, 5, 7, 8, 10, 12}
    if (year % 4 == 0 or year % 400 == 0) and year % 100 != 0:
        leafYear = True
    else:
        leafYear = False
    if month in dal:
        return 31
    else:
        if month == 2:
            if leafYear:
                return 28
            else:
                return 29
        else:
            return 30

print(days2(int(input("달을 입력해주세요: ")), int(input("월을 입력해주세요: "))))
