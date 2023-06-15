import sys
sys.path.append("..") 
from pythonds.basic.queue import Queue
def hotpotato(list,num):
    q1=Queue()
    for i in list:
        q1.enqueue(i)
    while q1.size()>1:
        for i in range(num):
            q1.enqueue(q1.dequeue())
        q1.dequeue()
    return q1.front()
    
