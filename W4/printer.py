import sys,random
sys.path.append("..") 
from pythonds.basic.queue import Queue

class Printer:
    def __init__(self,pageperminute):
        self.pageRate=pageperminute
        self.currentTask=None
        self.remainingTime=0
    
    def tick(self):
        if self.currentTask!=None:
            self.remainingTime-=1
        if self.remainingTime<=0:
            self.currentTask=None
    
    def busy(self):
        if self.currentTask!=None:
            return True
        else:
            return False
    
    def startNext(self,newTask):
        self.currentTask=newTask
        self.remainingTime=newTask.getPages()/self.pageRate*60

class Task:
    def __init__(self,time):
        self.timestamp=time
        self.pages=random.randrange(1,21)
    
    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self,currentTime):
        return currentTime-self.timestamp
        
def newPrintTask():
    num=random.randrange(1,181)
    if num==1:
        return True
    else:
        return False

def SimPrint(totalsec,pageperminute):
    p1=Printer(pageperminute)
    q1=Queue()
    l1=[]
    l2=[]
    time=0
    for i in range(totalsec):
        time+=1
        if newPrintTask():
            task1=Task(time)
            q1.enqueue(task1)
        if not p1.busy() and q1.size()!=0:
            l1.append(q1.peek().waitTime(time))
            p1.startNext(q1.dequeue())
            l2.append(q1.size())
        p1.tick()
    # print('{:.2f} sec'.format(sum(l1)/len(l1)),';{} remaining'.format(l2[-1]))
    return sum(l1)/len(l1)





        

