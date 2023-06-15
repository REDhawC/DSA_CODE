from pythonds.basic.stack0 import Stack0

def toback(ss):
    temps=Stack0()
    l1=[]
    for i in ss:
        l1.append(i)
    print(l1)
    index=0
    l2=[]
    while index<len(ss):
        if l1[index] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789':
            l2.append(l1[index])
        elif l1[index]=='(':
            temps.push(l1[index])
        elif l1[index]==')':
            while temps.peek()!='(':
                top=temps.pop()
                l2.append(top)
        elif l1[index] in '+-*/':
            if l1[index] in '*/':
                temps.push(l1[index])
            else:
                if temps.ifempty():
                    temps.push(l1[index])
                else:
                    while temps.peek() in '*/':
                        l2.append(temps.pop())
                    temps.push(l1[index])
        index+=1
    while temps.size()!=0:
        top2=temps.pop()
        if top2 not in '(':
            l2.append(top2)
    final=''.join(l2)
    return final

            

            
