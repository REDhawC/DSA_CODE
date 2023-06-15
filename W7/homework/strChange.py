opList = {'copy': 1, 'insert': 1, 'delete': 1}


def strChange(origin, target, operationList):
    score = 0
    operations = []
    origin = '_'+origin
    target = '_'+target
    table = {(i, j): 0 for i in range(len(origin))
             for j in range(len(target))}
    print(type(table))
    # 处理最左和最右两种情况
    for i in range(1, len(origin)):
        table[(i, 0)] = i*operationList['delete']
    for j in range(1, len(target)):
        table[(0, j)] = j*operationList['insert']
    # 根据公式列出 左,左上,上 3种情况进行填充
    for i in range(1, len(origin)):
        for j in range(1, len(target)):
            if origin[i]==target[j]:
                table[(i,j)]=table[(i-1,j-1)]
            else:
                table[(i,j)]=min(table[(i-1,j-1)],table[(i,j-1)],table[(i-1,j)])+1
    return table,origin[1:],target[1:],table[(len(origin)-1,len(target)-1)]

            # for i in range(1, len(origin)):
            #     for j in range(1, len(target)):
            #         options = []
            #         # the same ending letter
            #         if origin[i] == target[j]:
            #             options.append(
            #                 [table[(i-1, j-1)][0], 'copy:'+target[j]])
            #         # normal situations
            #         options.append(
            #             [table[(i, j-1)][0]+operationList['delete'], 'delete:'+origin[i]])
            #         options.append(
            #             [table[(i-1, j)][0]+operationList['insert'], 'insert:'+target[j]])
            #         table[(i, j)] = min(options, key=lambda x: x[0])
            # score = table[i, j][0]
            # while i > 0 or j > 0:
            #     op = table[i, j][1]
            #     operations.insert(0, op)
            #     if 'copy' in op:
            #         i -= 1
            #         j -= 1
            #     elif 'delete' in op:
            #         i -= 1
            #     elif 'insert' in op:
            #         j -= 1
            # return score, operations, origin[1:], target[1:],table


strChange('newb', 'newejk', opList)
