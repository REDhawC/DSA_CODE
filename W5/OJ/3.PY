n=int(input())
ch=input()
blank=' '*len(ch)
pic=[[ch for col in range(n)] for row in range(n)]

def spski(n,top,left):
    if n==1:
        return 
    for row in range(3):
        for col in range(3):
            if row ==1 and col==1:
                for r1 in range(n//3):
                    for c1 in range(n//3):
                        pic[top+n//3+r1][left+n//3+c1]=blank
            else:
                spski(n//3,top+row*n//3,left+col*n//3)

spski(n,0,0)
for r in range(n):
    print(' '.join(pic[r]))