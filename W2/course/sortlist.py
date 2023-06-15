# import timeit
# import random
# for i in range(10000, 1000001, 20000):
#     t = timeit.Timer('x.append(y)',
#                      'from __main__ import random,y,x')
#     x = list(range(2))
#     y= list(range(2))
#     lst_time = t.timeit(number=1000)
# #调用timer在list中找随机数找1000次
#     # x ={j:None for j in range(i)}
#     # dic_time = t.timeit(number=1000)
#     print('%d,%10.3f'% (i,lst_time))



import timeit
import random
for i in range(10000, 1000001, 20000):
    t = timeit.Timer('x[999]+=1',
                     'from __main__ import random,x')
    x ={j:1 for j in range(i)}
    lst_time = t.timeit(number=1000)
    print('%d,%10.3f'% (i,lst_time))