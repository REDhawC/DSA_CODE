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
for i in str1:
    if s1.isEmpty():
        s1.push(i)
    else:
        if s1.peek()==i:
            s1.pop()
        else:
            s1.push(i)
if len(s1)==0:
    print(None)
else:
    print(''.join(s1))


    



