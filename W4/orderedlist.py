class Node:
    def __init__(self,initdata):
        self.data=initdata
        self.next=None
    
    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data=newdata

    def setNext(self,newnext):
        self.next=newnext


class orderedList:
    def __init__(self):
        self.head=None
        
    def isEmpty(self):
        return self.head==None

    def size(self):
        count=0
        curNode=self.head
        while curNode!=None:
            count+=1
            curNode=curNode.getNext()
        return count

    def add(self,item):
        temp=Node(item)
        found=False
        previous=None
        curNode=self.head
        while not found:
            if self.head==None:
                self.head=temp
                break
            if curNode.getData()>item:
                if previous==None:
                    self.head=temp
                    temp.next=curNode         
                else:
                    previous.next=temp
                    temp.next=curNode
                found=True
            else:
                if curNode.next==None:
                    curNode.next=temp
                previous=curNode
                curNode=curNode.next
            return found



    def search(self,item):
        found=False
        temp=self.head
        while not found and temp.data!=None:
            if temp.getData()==item:
                found=True
            if temp.getData()>item:
                break
            if temp.next==None:
                break
            temp=temp.getNext()
            
        return found

    def remove(self,item):
        previous=None
        curNode=self.head
        found=False
        while not found:
            if curNode.getData()==item and curNode!=self.head:
                previous.next=curNode.next
                found=True
            elif curNode.getData()==item and curNode==self.head:
                self.head=curNode.next
                found=True
            if curNode.next==None:
                break
            if curNode.data>item:
                break
            previous=curNode
            curNode=curNode.next
            
        return 'o:found and removed?',found

