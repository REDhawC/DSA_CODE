def coinsDynamic(coinsValueList, change, cache):
    for i in range(1, change+1):
        minCoins = i
        # 对所有涉及到的coins情况,初始化最大值,
        # 就是min等于全部取1个硬币取完的情况
        for n in [v for v in coinsValueList if v <= i]:  # 对这一coins情况从币列表的所有可能方向进行循环
            if cache[i-n]+1 < minCoins:  # 如果是5,5-5=0,cache[0]=0,就出现了最优解
                minCoins = cache[i-n]+1
        cache[i] = minCoins  # 把最优解登记起来,下次就能查到前面的了,成功完成最优解检索
    return cache[change]


def coinsDynamic2(coinsValueList, change, bestCache, curCoin):
    for i in range(1, change+1):
        minCoins = i
        # 对所有涉及到的coins情况,初始化最大值,
        # 就是min等于全部取1个硬币取完的情况
        for n in [v for v in coinsValueList if v <= i]:  # 对这一coins情况从币列表的所有可能方向进行循环
            if bestCache[i-n]+1 < minCoins:  # 如果是5,5-5=0,cache[0]=0,就出现了最优解
                minCoins = bestCache[i-n]+1
                curCoin[i] = n
        bestCache[i] = minCoins  # 把最优解登记起来,下次就能查到前面的了,成功完成最优解检索
    return bestCache[change]


def printCoins(curCoin, change):
    while change > 0:
        print(curCoin[change])
        change = change-curCoin[change]


amount = 63
clist = [1, 5, 10, 21, 25]
coinsUsed = [0]*64
coinsCount = [0]*64
print(coinsDynamic2(clist, amount, coinsCount, coinsUsed))
printCoins(coinsUsed, amount)
