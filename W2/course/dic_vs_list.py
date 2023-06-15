import timeit
import random
for i in range(10000, 1000001, 20000):
    t = timeit.Timer('random.randrange(%d) in x' % i,
                     'from __main__ import random,x')
    x = list(range(i))
    lst_time = t.timeit(number=1000)
#调用timer在list中找随机数找1000次
    x ={j:None for j in range(i)}
    dic_time = t.timeit(number=1000)
    print('%d,%10.3f,%10.3f'% (i,lst_time,dic_time))