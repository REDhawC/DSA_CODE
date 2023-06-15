import sys,random
sys.path.append("..") 
from pythonds.basic.deque import Deque
def huiwen(ss): 
    d1=Deque()
    for i in ss:
        d1.addFront(i)
    correct=True
    while d1.size()>1 and correct:
        if d1.removeFront()!=d1.removeRear():
            correct=False
    return correct


