

def Hanoi4(n):
    cache=[None for i in range(n+1)]
    if cache[n]:
        return cache[n]
    if n==0:
        cache[n]=0
    elif n==1:
        cache[n]=1
    elif n==2:
        cache[n]=3
    else:
        l1=[]
        for i in range(1,n):
            l1.append(2*Hanoi4(i)+2**(n-i)-1)
        cache[n]=min(l1)
    return cache[n] 

from functools import lru_cache
@lru_cache(maxsize=128)

def Hanoi4lru(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n==2:
        return 3
    else:
        l1=[]
        for i in range(1,n):
            l1.append(2*Hanoi4(i)+2**(n-i)-1)
        return min(l1)
 

