
def Hanoi(num,start,mid,target):
    if num>0:
        Hanoi(num-1,start,target,mid)
        print('moving {} from {} to {}'.format(num,start,target))
        Hanoi(num-1,mid,start,target)

Hanoi(3,'A','B','C')
