import datetime as dt
d1 = dt.date(2022, 1, 1)
flist = []
for i in range(365):
    flist.append((d1+dt.timedelta(days=i)).strftime('%Y%m%d').encode())


import math as m
import time as t
start = t.time()
f = open("pi50.4.bin", 'rb')
d = f.read()
l1 = []
l2=[]
for i in d:
    sx = '{:02x}'.format(i)
    l1.append(sx)
full = ''.join(l1)
full=full.encode()
print(len(full), full[:20])
sub1 = 0
sub2 = 0
for i in flist:
    if full.find(i) == -1:
        sub2 = sub2+1
    else:
        sub1 = sub1+1

print('exists:', sub1, 'cant found', sub2)

end = t.time()
sub3 = end-start
print(sub3)
