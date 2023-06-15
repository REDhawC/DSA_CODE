a,b=input().split()
c=input()
b=int(b)

def tranM(num,base):
    re=0
    base=int(base)
    count=len(str(num))-1
    for i in str(num):
        i=int(i)*base**count
        re=re+i
        count-=1
    return re

def transDegits(num,base):
    digitList='0123456789ABCDEF'
    if num<base:
        return digitList[num]
    else:
        return transDegits(num//base,base)+digitList[num%base]

print(transDegits(tranM(c,a),b))
