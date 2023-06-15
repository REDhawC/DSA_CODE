# ======= 2 基数排序 =======
# 实现一个基数排序算法，用于10进制的正整数从小到大的排序。
#
# 思路是保持10个队列(队列0、队列1......队列9、队列main)，开始，所有的数都在main队列，没有排序。
# 第一趟将所有的数根据其10进制个位(0~9)，放入相应的队列0~9，全放好后，按照FIFO的顺序，将每个队列的数合并排到main队列。
# 第二趟再从main队列队首取数，根据其十位的数值，放入相应队列0~9，全放好后，仍然按照FIFO的顺序，将每个队列的数合并排到main队列。
# 第三趟放百位，再合并；第四趟放千位，再合并。
# 直到最多的位数放完，合并完，这样main队列里就是排好序的数列了。
#
# 创建一个函数，接受参数为一个列表，为需要排序的一系列正整数，
# 返回排序后的数字列表。
# 输入样例1：
# [1, 2, 4, 3, 5]
# 输出样例1：
# [1, 2, 3, 4, 5]
# 输入样例2：
# [8, 91, 34, 22, 65, 30, 4, 55, 18]
# 输出样例2：
# [4, 8, 18, 22, 30, 34, 55, 65, 91]


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def radix_sort(s) -> list:
    # 请在此编写你的代码（可删除pass语句）
    main=Queue()
    for i in s:
        main.enqueue(i)
    q1=Queue()
    q2=Queue()
    q3=Queue()
    q4=Queue()
    q5=Queue()
    q6=Queue()
    q7=Queue()
    q8=Queue()
    q9=Queue()
    q0=Queue()
    t=0
    l2=[]
    sz=main.size()
    while t<sz:
        t=t+1
        item=main.dequeue()
        one=str(item)[-1]
        l2.append(one)
        eval('q'+one).enqueue(item)
    for i in [9,8,7,6,5,4,3,2,1,0]:
        while not eval('q'+str(i)).isEmpty():
            main.enqueue(eval('q'+str(i)).dequeue())
    t=0
    while t<sz:
        t=t+1
        item=main.dequeue()
        if len(str(item))==1:
            q0.enqueue(item)
        else:
            ten=str(item)[-2]
            l2.append(ten)
            eval('q'+ten).enqueue(item)
    for i in [9,8,7,6,5,4,3,2,1,0]:
        while not eval('q'+str(i)).isEmpty():
            main.enqueue(eval('q'+str(i)).dequeue())

    return main.items

    # for i in range(10):
    #     while not eval('q'+str(i)).isEmpty():
    #         main.enqueue(eval('q'+str(i)).dequeue())
            


        
    

    



    # 代码结束


# 调用检验
print("======== 2-radix_sort ========")
print(radix_sort([1, 2, 4, 3, 5]))
print(radix_sort([8, 91, 34, 22, 65, 30, 4, 55, 18]))
print(radix_sort([22,22,33,34,12,39,78,9]))