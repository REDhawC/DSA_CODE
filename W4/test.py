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
    return s1.peek()



# s1=Stack()
# s1.push('3333')
# s1.push('3443')
# s1.push('31111')
# print(s1)

