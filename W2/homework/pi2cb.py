import datetime as dt
import time as t
st=t.time()
f = open('pi50.4.bin', 'rb')
dbuff = f.read()
s = (''.join((f'{d:02x}' for d in dbuff))).encode()
d1 = dt.date(2022, 1, 1)
found = 0
for n in range(365):
    day = ((d1+dt.timedelta(days=n)).strftime('%Y%m%d')).encode()
    if day in s:
        found += 1
print(found)
end=t.time()
tt=end-st
print(tt)