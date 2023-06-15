import datetime as dt
import time as t
st=t.time()
f = open('pi50.4.bin', 'rb')
dbuff = f.read()
ls=[]
for i in dbuff:
    si='{:02x}'.format(i)
    ls.append(si)
s=(''.join(ls)).encode()
d1 = dt.date(2022, 1, 1)
days={((d1+dt.timedelta(days=n)).strftime('%m%d')).encode() for n in range(365)}
find=0
pos=s.find(b'2022')
while pos>=0:
    if s[pos+4:pos+8] in days:
        find+=1
        days.remove(s[pos+4:pos+8])
    pos=s.find(b'2022',pos+1)


# while pos>=0:
#     pnum=s[pos+4:pos+8]
#     if pnum in l1:
#         find+=1
#         l1.remove(pnum)
#     pos=s.find(b'2022',pos+1)

end=t.time()
print(end-st,'s')