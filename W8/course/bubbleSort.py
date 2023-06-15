l1 = [1, 2, 3, 1, 28, 21]


def bubbleSort(list):
    for i in range(len(list)-1, 0, -1):
        for k in range(i):
            if list[k] > list[k+1]:
                list[k], list[k+1] = list[k+1], list[k]
    return list


bubbleSort(l1)


def improvedBubbleSort(list):
    totalNum = len(list)-1
    exchange = True
    while exchange and totalNum>0:
        exchange = False
        for k in range(totalNum):
            if list[k] > list[k+1]:
                exchange=True
                list[k], list[k+1] = list[k+1], list[k]
        totalNum-=1
    return list
