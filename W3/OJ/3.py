class Stack(list):
    def push(self,item):
        self.append(item)
    def peek(self):
        return self[-1]
    def size(self):
        return len(self)
    def isEmpty(self):
        return self==[]

str1=input()
s1=Stack()
l1=[]
for i in str1:
    c=int(i)
    if s1.isEmpty():
        s1.push(c)
    else:
        if s1.peek()>c:
            s1.push(c)
        else:
            while not s1.isEmpty():
                l1.append(str(s1.pop()))
            s1.push(c)
while not s1.isEmpty():
    l1.append(str(s1.pop()))
if ''.join(l1) in '0123456789':
    print('Yes')
else:
    print('No')
    
#1043259876

    



