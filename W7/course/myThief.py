goodsDic = {1: {'weight': 2, 'value': 3},
            2: {'weight': 3, 'value': 4},
            3: {'weight': 4, 'value': 8},
            4: {'weight': 5, 'value': 8},
            5: {'weight': 9, 'value': 10}, }
maxWeight = 20


def myThief(goods, maxW):
    #绘制table
    table = {(item, curWeight): 0 for item in range(len(goods)+1)
             for curWeight in range(maxW+1)}
    print(table)
    # 已经初始化了最左和最右,全都是0
    for i in range(1, len(goods)+1):
        for w in range(1, maxW+1):
            if w < goods[i]['weight']:
                # 放不下第i件good的话,直接就等于不放i的[i-1,w]的价值
                table[(i, w)] = table[(i-1, w)]
            else:
                # 如果放得下,需要比较出2种情况的最大值:
                # 1:不放i的[i-1,w]的价值 ; 2:放了i的价值(i的价值+[i-1,w-i的重量])
                table[(i, w)] = max(table[(i-1, w-goods[i]['weight'])] +
                                    goods[i]['value'], table[(i-1, w)])
    return table[(len(goods), maxW)]


myThief(goodsDic, maxWeight)
