class Stack(list):
    def push(self,item):
        self.append(item)
    def peek(self):
        return self[-1]
    def size(self):
        return len(self)
    def isEmpty(self):
        return self==[]

s1=Stack()
dic1={'(':')','{':'}','[':']'}
str1=str(input())
correct=True
index=0

while correct and index<len(str1):
    if s1.isEmpty():
        if str1[index] in '({[':
            s1.push(str1[index])
        else:
            correct=False 
    else:
        if str1[index] in '({[':
            s1.push(str1[index])
        elif str1[index] in ']})':
            if dic1[s1.peek()]==str1[index]:
                s1.pop()
            else:
                correct=False
    index+=1
if not s1.isEmpty():
    correct=False
print(correct)
    



