import arrow
date_list = []
for year in [2022]:  # 年份
    start_date = '%s-1-1' % year
    a = 0
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_sum = 366
    else:
        days_sum = 365
    while a < days_sum:
        b = arrow.get(start_date).shift(days=a).format("YYYYMMDD")
        a += 1
        date_list.append(b)
for date in date_list:
    print(date)