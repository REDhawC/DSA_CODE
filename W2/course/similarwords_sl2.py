def check2(s1,s2):
    l1=list(s1)
    l2=list(s2)
    l1.sort()
    l2.sort()
    pos1=0
    ifOK=True
    while pos1<len(l1) and ifOK:
        
        if l1[pos1]!=l2[pos1]:
            ifOK=False
        pos1=pos1+1
    return ifOK

# s='fhueiwohfoiau'
# l1=list(s)
# print(l1)
# l1.sort()
# print(l1)

