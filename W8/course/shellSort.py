l1 = [1, 2, 3, 4, 66, 23, 11, 24]


def shellSort(list):
    subListCount = len(list)//2  # 子列表数量减半
    while subListCount > 0:
        # 当子列表数量=1的时候是最后一次,等于进行全体的insertSort
        for startPos in range(subListCount):  # 子列表有多少个,起始位置就有多少个
            gapInsertionSort(list, startPos, subListCount)
        print('After increments of size', subListCount,
              ',\nthe list is', list)
        subListCount = subListCount//2  # 数量再减半


def gapInsertionSort(list, start, gap):
    # 起始位置+gap就是得到序列中的第二项,然后再以gap为step,就能摘出这一组子列表
    for num in range(start+gap, len(list), gap):
        currentValue = list[num]  # 当前对比项,将它从当前位置选取上来
        position = num  # 当前位置
        while position > 0 and list[position-gap] > currentValue:
            # 如果前面那个数[子列表中的第一个数]比当前数大,那就前面的数占领当前position
            list[position] = list[position-gap]
            position -= gap
            # 当前数相应的位置往前挪1个,继续去跟前1个数对比
        list[position] = currentValue
        # 如果前面那个数比currentValue小/CV到最前面了,
        # 就把现在这个位置给CV
    return list


shellSort(l1)
