# def sl3(s1,s2):
#     c1=[0]*26
#     c2=[0]*26
#     pos1=0
#     for i in range(len(s1)):
#         pos=ord(s1[i])-ord('a')
#         c1[pos]=c1[pos]+1
#     for i in range(len(s2)):
#         pos=ord(s2[i])-ord('a')
#         c2[pos]=c2[pos]+1
#     ifOK=True
#     for i in range(26):
#         if c1[i]!=c2[i]:
#             ifOK=False
#     return ifOK


def sl3(s1,s2):
    d1={}
    d2={}
    pos1=0
    for i in s1:
        if i in d1:
            d1[i]=d1[i]+1
        else:
            d1[i]=1
    for i in s2:
        if i in d2:
            d2[i]=d2[i]+1
        else:
            d2[i]=1
    ifOK=True
    if len(d1)!=len(d2):
        return False
    for i in s1:
        if d1[i]!=d2[i]:
            ifOK=False
    return ifOK


