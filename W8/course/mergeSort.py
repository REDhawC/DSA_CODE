l1 = [1, 2, 3, 4, 66, 23, 11, 7, 45]


def mergeSort(list):
    if len(list) > 1:
        # 如果分完的一边数据量>1就还得分,到只剩1个数据为止
        mid = len(list)//2
        left_half = list[:mid]
        right_half = list[mid:]
        print(left_half, right_half)
        # 要注意总表的数据量一直是没有变的,
        # 可以理解为不断的分裂,母体还保持不变 [因此导致占用内存较大]
        mergeSort(left_half)
        mergeSort(right_half)
        leftIndex = rightIndex = totalIndex = 0
        # 设置3个表的索引,total是被分的总表
        while leftIndex < len(left_half) and rightIndex < len(right_half):
            if left_half[leftIndex] < right_half[rightIndex]:
                list[totalIndex] = left_half[leftIndex]
                # 对应在总表中加入最小值
                leftIndex += 1
                totalIndex += 1
            else:
                list[totalIndex] = right_half[rightIndex]
                rightIndex += 1
                totalIndex += 1
        # 下面用来处理left和right里面个数不一致导致被剩下的数据,
        # 无需比较,直接修改到最后.[因为一般就只会剩下1个最大的]
        while leftIndex < len(left_half):
            list[totalIndex] = (left_half[leftIndex])
            leftIndex += 1
            totalIndex += 1

        while rightIndex < len(right_half):
            list[totalIndex] = (right_half[rightIndex])
            rightIndex += 1
            totalIndex += 1
        return list


def pyMergeSort(list):
    if len(list) <= 1:
        return list
    mid = len(list)//2
    left = pyMergeSort(list[:mid])
    right = pyMergeSort(list[mid:])
    print(left, right)
    merged = []
    while left and right:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    while right:
        merged.append(right.pop(0))
    while left:
        merged.append(left.pop(0))
    return merged


# mergeSort(l1)
pyMergeSort(l1)
