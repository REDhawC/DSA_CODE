def recMC(coinValueList, change):
    minCoins = change  # 可以理解成暴力解的全换成1块钱.
    print(minCoins)
    if change in coinValueList:
        return 1
    else:
        for i in [c for c in coinValueList if c <= change]:
            num = 1+recMC(coinValueList, change-i)  # 每条路径的结果进行累加
            print('N', num)
            if num < minCoins:  # 这个比较是真的骚...当前层级的4条路,看下谁目前最少
                minCoins = num  # 就设置为新的min,然后传回上一级
                print('C', minCoins)
    return minCoins


def recMC2(coinValueList, change, resultList):
    minCoins = change  # 可以理解成暴力解的全换成1块钱.
    if change in coinValueList:
        resultList[change] = 1
        return 1
    if resultList[change] > 0:
        return resultList[change]
    else:
        for i in [c for c in coinValueList if c <= change]:
            num = 1+recMC2(coinValueList, change-i, resultList)
            if num < minCoins:  # 这个比较是真的骚...当前层级的4条路,看下谁目前最少
                minCoins = num  # 就设置为新的min,然后传回上一级
                resultList[change] = minCoins
    return minCoins
