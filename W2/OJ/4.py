a=int(input())
b=int(input())
t2=0
for k in range(a,b+1): 
    t=0
    for i in range(1,k+1):
        
        if k%i==0:
            t+=1
    if t==2:
        t2+=1
print(t2)