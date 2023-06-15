tr = [None, {'w': 2, 'v': 3},
      {'w': 3, 'v': 4},
      {'w': 4, 'v': 8},
      {'w': 5, 'v': 8},
      {'w': 9, 'v': 10}]

max_w = 20

M = {(i, w): 0 for i in range(len(tr))
     for w in range(max_w+1)}


def thief(goodsList, maxWeight, m):
    for i in range(1, len(goodsList)):
        for w in range(1, maxWeight+1):
            if goodsList[i]['w'] > w:
                m[(i, w)] = m[(i-1, w)]
            else:
                m[(i, w)] = max(m[(i-1, w)], m[(i-1, w-tr[i]['w'])]+tr[i]['v'])
    return m[len(goodsList)-1, maxWeight], m

print(M)


tr2 = {(2, 3),
       (3, 4),
       (4, 8),
       (5, 8),
       (9, 10)
       }

M2 = {}


def thiefR(goodsList, maxWeight, m):
    if goodsList == set() or maxWeight == 0:
        m[(tuple(goodsList), maxWeight)] = 0
        return 0
    elif (tuple(goodsList), maxWeight) in m:
        return m[(tuple(goodsList), maxWeight)]
    else:
        maxValue = 0
        for i in goodsList:
            if i[0] <= maxWeight:
                v = thiefR(goodsList-{i}, maxWeight-i[0], m)+i[1]
                maxValue = max(v, maxValue)
        m[(tuple(goodsList), maxWeight)] = maxValue
        return maxValue
