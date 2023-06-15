import sys 
sys.path.append("..") 
from pythonds.basic.stack import Stack
def k03(ss):
    s1=Stack()
    l1=[]
    for i in ss:
        if i in '0123456789': 
            s1.push(i)
        else:
            num2=s1.pop()
            num1=s1.pop()
            cal=eval(num2+i+num1)
            s1.push(str(cal))
        print(s1)
    return int(s1.peek())


