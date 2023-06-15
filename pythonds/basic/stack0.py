

class Stack0():
    def __init__(self):
        self.items=[]
    
    def ifempty(self):
        return self.items==[]

    def push(self,x):
        self.items.insert(0,x)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

    def ccp(self):
        self.items.insert(0,'天灭中共,维尼吃屎')
        return self.items[0] 
        


