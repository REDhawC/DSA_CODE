import big_o as bo
import timeit as tt
def fun1(x):
    l1=[1,2,3]
    l1.insert(0,x)


def fun2(x):
    l1=[1,2,3]
    l1.append(x)

bof11,bof12=bo.big_o(
    fun1
    ,data_generator=lambda n: bo.datagen.integers(n,10000,100000)
    ,min_n=10
    ,max_n=11
    ,n_measures=1000
    ,)

bof21,bof22=bo.big_o(
    fun2
    ,data_generator=lambda n: bo.datagen.integers(n,10000,100000)
    ,min_n=10
    ,max_n=11
    ,n_measures=1000
    ,)

print('fun1(bigo):',bof11,'fun2(bigo):',bof21)

x=[i for i in range(10000,100001,10000)]

for i in range(10000,1000001,10000):
    l=[n for n in range(i)]
    t1 = tt.Timer('fun1(l)',
                        'from __main__ import fun1,l')
    t2 = tt.Timer('fun2(l)',
                        'from __main__ import fun2,l')
    time1=t1.timeit(number=1000)
    time2=t2.timeit(number=1000)
    print('%d,%10.3f,%10.3f'% (i,time1,time2))

