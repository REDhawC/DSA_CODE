class Stack(list):
    def push(self,item):
        self.append(item)
    def peek(self):
        return self[-1]
    def size(self):
        return len(self)
    def isEmpty(self):
        return self==[]

st=Stack()
s=input()
n=0
i=0
while i <10 and n<10:
    k=int(s[i])
    if n<=k:
        for m in range(n,k+1):
            st.push(m)
        n=k+1
    else:
        break
    while not st.isEmpty() and st.peek()==int(s[i]):
        m=st.pop()
        i+=1

if st.isEmpty():
    print('Yes')
else:
    print('No')