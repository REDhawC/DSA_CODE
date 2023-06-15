l1 = [1, 2, 3, 4, 66, 23, 11]


def insertSort(list):
    for num in range(1, len(list)):
        currentValue = list[num]  # 当前对比项,将它从当前位置选取上来
        position = num  # 当前位置
        while position > 0 and list[position-1] > currentValue:
            # 如果前面那个数比当前数大,那就前面的数占领当前position
            list[position] = list[position-1]
            position -= 1
            # 当前数相应的位置往前挪1个,继续去跟前1个数对比
        list[position] = currentValue
        # 如果前面那个数比currentValue小/CV到最前面了,
        # 就把现在这个位置给CV
        print(list)
    return list


insertSort(l1)
