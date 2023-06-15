import math as m
f = open("pi50.4.bin", 'rb')
# f.seek(10100049, 0)
# p2 = f.tell()
# print('p2:', p2)
# d2 = f.read(5)
# a1 = ''
# for a in d2:
#     print(hex(a))
#     sx = hex(a).replace('0x', '')
#     a1 = a1+sx
# print(a1)

# d1={}
# v=0
# for a in d:
#     v=v+1
#     d1[v]=hex(a)
#     print(hex(a),d1[v])
# f.close

def pi(a,num):
    f = open("pi50.4.bin", 'rb')
    
    f.seek(m.floor(a/2), 0)
    d=f.read(num)
    a=''
    for i in d:
        sx = hex(i).replace('0x', '')
        if len(a)<num:
            a=a+sx
        if len(a)>num:
            a=a[:-len(sx)]
    return a,len(a)

