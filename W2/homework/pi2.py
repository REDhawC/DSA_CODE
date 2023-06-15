# import math as m
# f = open("pi50.4.bin", 'rb')
# d=f.read(50000000)
# a=''
# for i in d:
#     sx = hex(i).replace('0x', '')
#     a=a+sx
# print(len(a))

# def find(ss):
#     if ss in a:
#         return a.index(ss)
#     else:
#         print('NOT FOUND')
# import arrow
# date_list = []
# for year in [2022]:  # 年份
#     start_date = '%s-1-1' % year
#     a = 0
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         days_sum = 366
#     else:
#         days_sum = 365
#     while a < days_sum:
#         b = arrow.get(start_date).shift(days=a).format("YYYYMMDD")
#         a += 1
#         date_list.append(b)
# for date in date_list:
#     print(date)
    
import datetime as dt
d1=dt.date(2022,1,1)
flist=[]
for i in range(365):
    flist.append((d1+dt.timedelta(days=i)).strftime('%Y%m%d'))

def check2022():
    import math as m
    import time as t
    start=t.time()
    f = open("pi50.4.bin", 'rb')
    d=f.read(50000000)
    l1=[]
    for i in d:
        sx = hex(i).replace('0x', '')
        l1.append(sx)
    full=''.join(l1)
    print(len(full),full[:20])
    sub1=0
    sub2=0
    for i in flist:
        if full.find(i)==-1:
            sub2=sub2+1
        else:
            sub1=sub1+1

    print('exists:',sub1,'cant found',sub2)

    end=t.time()
    sub3=end-start
    print(sub3)


