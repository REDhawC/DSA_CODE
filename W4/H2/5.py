# ======== 5 双链无序表 ========
# 实现双向链表版本的UnorderedList，接口同ADT UnorderedList
# 包含如下方法：isEmpty, add, search, size, remove, append，index，pop，insert, __len__, __getitem__
# 用于列表字符串表示的__str__方法 (注：__str__里不要使用str(), 用repr()代替
# 用于切片的__getitem__方法
# 在节点Node中增加prev变量，引用前一个节点
# 在UnorderedList中增加tail变量与getTail方法，引用列表中最后一个节点
# 选做：DoublyLinkedList(iterable) -> new DoublyLinkedList initialized from iterable's items
# 选做：__eq__, __iter__
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


class DoublyLinkedList():
    # 请在此编写你的代码（可删除pass语句）
    def __init__(self) -> None:
        self.head=None

    def __len__(self):
        count=0
        curNode=self.head
        if self.head==None:
            return count
        else:
            while curNode!=None:
                count+=1
                curNode=curNode.next
            return count

    def isEmpty(self):
        return self.head==None
    
    def add(self,item):
        temp=Node(item)
        curNode=self.head
        if curNode==None:
            self.head=temp
        else:
            while curNode.next!=None:
                curNode=curNode.next
            curNode.next=temp
            temp.prev=curNode

    def size(self):
        count=0
        curNode=self.head
        if self.head==None:
            return count
        else:
            while curNode!=None:
                count+=1
                curNode=curNode.next
            return count

    def search(self,item):
        temp=Node(item)
        curNode=self.head
        if curNode==None:
            return False
        while curNode!=None:
            if curNode.data==temp.data:
                return True
            else:
                curNode=curNode.next
        return False

    def remove(self,item):
        temp=Node(item)
        curNode=self.head
        if curNode==None:
            pass
        while curNode!=None:
            if curNode.data==temp.data:
                if curNode.prev==None:
                    if curNode.next==None:
                        self.head=None
                        break
                    else:
                        curNode.next.prev=None
                        self.head=curNode.next
                        break
                else:
                    if curNode.next==None:
                        curNode.prev.next=None
                        break
                    else:
                        curNode.next.prev=curNode.prev
                        curNode.prev.next=curNode.next
                        break
            else:
                curNode=curNode.next
        

    def append(self,item):
        temp=Node(item)
        if self.head==None:
            self.head=temp
        else:
            self.head.prev=temp
            temp.next=self.head
            self.head=temp

    def index(self,item):
        temp=Node(item)
        count=0
        curNode=self.head
        if curNode==None:
            return 'Not found!'
        while curNode!=None:
            if curNode.data==temp.data:
                return self.size()-count-1
            else:
                curNode=curNode.next
                count=count+1
        return 'Not found!'

    def pop(self,pos=0):
        if pos==0:
            if self.head==None:
                return None
            else:
                popitem=self.head
                if self.head.next==None:
                    self.head=None
                    return popitem.data
                else:
                    self.head.next.prev=None
                    self.head=self.head.next
                    return popitem.data
        else:
            count=0
            pos=self.size()-pos-1
            curNode=self.head
            while count!=pos:
                curNode=curNode.next
                count+=1
            temp=curNode.data
            curNode.prev.next=curNode.next
            curNode.next.prev=curNode.prev
            return temp
            

    def insert(self,pos,item):
        pos=self.size()-pos
        count=0
        temp=Node(item)
        curNode=self.head
        while count!=pos:
            curNode=curNode.next
            count+=1
        if pos==0:
            temp.next=self.head
            self.head.prev=temp
            self.head=temp
        else:   
            temp.next=curNode
            curNode.prev.next=temp
            temp.prev=curNode.prev
# 包含如下方法：isEmpty, add, search, size, remove, append，index，pop，insert, __len__, __getitem__

    def __str__(self):
        l1=[]
        count=0
        curNode=self.head
        while curNode!=None:
            temp=curNode.data
            l1.insert(0,temp)
            curNode=curNode.next
        return str(l1)
        
    __repr__=__str__
    

    def __getitem__(self,type):
        if isinstance(type,int):
            pos=self.size()-type-1
            curNode=self.head
            count=0
            while count<pos:
                count+=1
                curNode=curNode.next
            return curNode.data
        elif isinstance(type,slice):
            if type.start==None:
                Start=0
            else:
                Start=type.start
            if type.stop==None:
                Stop=self.size()
            else:
                Stop=type.stop
            if type.step==None:
                Step=1
            else:
                Step=type.step
            pos=self.size()-Start-1
            curNode=self.head
            count=0
            dcopy=DoublyLinkedList()
            while count<pos:
                count+=1
                curNode=curNode.next
            newcount=0
            while newcount<Stop-Start and curNode!=None:
                
                if Step==1:
                    dcopy.append(curNode.data)
                else:
                    if newcount%Step==0:
                        dcopy.append(curNode.data)
                newcount=newcount+1
                curNode=curNode.prev
            return dcopy



            


        


    # 代码结束


# # 检验
print("======== 5-DoublyLinkedList ========")
mylist = DoublyLinkedList()
for i in range(0, 20, 2):
    mylist.append(i)
mylist.add(3)
mylist.remove(6)
# print(mylist.getTail().getPrev().getData())  # 16
print(mylist.isEmpty())  # False
print(mylist.search(5))  # False
print(mylist.size())  # 10
print(mylist.index(2))  # 2
print(mylist.pop())  # 18
print(mylist.pop(2))  # 2
print(mylist)  # [3, 0, 4, 8, 10, 12, 14, 16]
mylist.insert(3, "10")
print(len(mylist))  # 9
print(mylist[4])  # 8
print(mylist)  # ?
print(mylist[3:8:2])  # ['10', 10, 14]
# print(mylist[3:8])
# print(mylist[3:8:1])


