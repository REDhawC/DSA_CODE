class Node():
    def __init__(self, initdata=None):
        self.data = initdata
        self.next = None
        self.prev = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

    def setPrev(self, newprev):
        self.prev = newprev
# ======== 4 链表实现栈和队列 ========
# 用链表实现ADT Stack与ADT Queue的所有接口
class LinkStack():
    # 请在此编写你的代码（可删除pass语句）
    def __init__(self) -> None:
        self.end=None

    def push(self,item):
        temp=Node()
        temp.data=item
        if self.end==None:
            self.end=temp
            
        else:
            self.end.next=temp
            temp.prev=self.end
            self.end=temp

    def size(self):
        curNode=self.end
        count=0
        while curNode!=None:
            count+=1
            curNode=curNode.prev
        return count

    def peek(self):
        return self.end.data
    
    def isEmpty(self):
        return self.end==None
            
    def pop(self):
        if self.end==None:
            return None
        else:
            temp=self.end
            if self.end.prev!=None:
                self.end.prev.next=None
            self.end=self.end.prev
            return temp.data    
    # 代码结束

class LinkQueue():
    # 请在此编写你的代码（可删除pass语句）
    def __init__(self) -> None:
        self.front=None
        self.end=None
    
    def enqueue(self,item):
        temp=Node(item)
        if self.front==None:
            self.front=temp
        else:
            temp.next=self.front
            self.front.prev=temp
            self.front=temp

    def size(self):
        if self.front==None:
            return 0
        else:
            count=0
            curNode=self.front
            while curNode!=None:
                count+=1
                curNode=curNode.next
            return count
    
    def dequeue(self):
        temp=self.front
        if temp==None:
            return None
        while temp.next!=None:
            temp=temp.next
        if temp.next==None and temp.prev==None:
            self.front=None
        else:
            temp.prev.next=None
            temp.prev=None
        return temp.data

    def isEmpty(self):
        return self.front==None

    # 代码结束


# 检验
print("======== 4-Link Stack & Link Queue ========")
s = LinkStack()
q = LinkQueue()
for i in range(10):
    s.push(i)
    q.enqueue(i)
print(s.peek(), q.dequeue())  # 9 0
print(s.pop(), q.size())  # 9 9
while not s.isEmpty():
    s.pop()
print(s.size(), q.isEmpty())  # 0 False