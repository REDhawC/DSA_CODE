from pythonds.basic.stack0 import Stack0
def domath(a,b,type):
    ss=a+type+b
    ss=eval(ss)
    return ss

def backcal(ss1):
    l1=[]
    temp=Stack0()
    for i in ss1:
        l1.append(i)
    print(l1)
    for i in l1:
        if i in '0123456789':
            temp.push(i)
        elif i in '+-*/':
            num2=temp.pop()
            num1=temp.pop()
            rst=domath(num1,num2,i)
            temp.push(str(rst))
    return rst

