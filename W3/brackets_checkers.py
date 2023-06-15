from pythonds.basic.stack0 import Stack0

def bramatch(a,b):
    if a in '<([{' :
        return '<([{'.index(a)=='>)]}'.index(b)
    else:
        return False


def bracketscheck(ss):
    s=Stack0()
    index=0
    proper=True
    ss=ss.replace(' ','')
    while index<len(ss) and proper:
        if ss[index] in '<([{':
            s.push(ss[index])
        else:
            if ss[index] not in '>)]}':
                proper=False
            elif s.ifempty():
                proper=False
            elif bramatch(s.peek(),ss[index]):
                s.pop()
            else:
                proper=False
        index+=1
    if s.ifempty() and proper:
        return True
    else:
        return False

