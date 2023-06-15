from timeit import Timer



def test1():
    l=[]
    for i in range(1000):
        l=l+[i]

def test2():
    l=[]
    for i in range(1000):
        l.append(i)

def test3():
    l=[i for i in range(1000)]


def test4():
    l=list(range(1000))

# if __name__ == '__main__':


for i in range(1000000,100000001,1000000):
    x=list(range(i))
    pop1=Timer('x.pop(0)',setup='from __main__ import x')
    print('pop1:',pop1.timeit(number=1000))
    pop2=Timer('x.pop()',setup='from __main__ import x')
    print('pop2:',f"{pop2.timeit(number=1000):f}")

    # t1=Timer('test1()',setup='from __main__ import test1')
    # print(t1.timeit(number=1000))
    
    # t2=Timer('test2()',setup='from __main__ import test2')
    # print(t2.timeit(number=1000))

    # t3=Timer('test3()',setup='from __main__ import test3')
    # print(t3.timeit(number=1000))

    # t4=Timer('test4()',setup='from __main__ import test4')
    # print(t4.timeit(number=1000))