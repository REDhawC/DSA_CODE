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


class UnorderedList:
    def __init__(self):
        self.head=None
        
    def isEmpty(self):
        return self.head==None

    def add(self,value):
        temp=Node(value)
        temp.setNext(self.head)
        self.head=temp

    def size(self):
        count=0
        curNode=self.head
        while curNode!=None:
            count+=1
            curNode=curNode.getNext()
        return count

    def search(self,item):
        found=False
        temp=self.head
        while not found:
            if temp.getData()==item:
                found=True
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
            previous=curNode
            curNode=curNode.next
            
        return 'found and removed?',found




        
    

        
