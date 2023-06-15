import time as t
def check(s1, s2):
    start=t.time()
    l2 = list(s2)
    if len(s1) == len(s2):
        ifOK = True
        pos1 = 0
        while ifOK and pos1 < len(s1):
            pos2 = 0
            find = False
            while not find and pos2 < len(l2):
                if s1[pos1] == s2[pos2]:
                    find = True
                else:
                    pos2 = pos2+1
            if not find:
                ifOK = False
            else:
                l2[pos2] = None
            pos1 = pos1+1
    else:
        ifOK = False
    end=t.time()
    total=end-start
    print(total)
    return ifOK
