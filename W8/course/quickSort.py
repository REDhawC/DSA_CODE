l1 = [1, 2, 3, 4, 66, 23, 11, 7, 45]


def quickSort(list):
    quickSortHelper(list, 0, len(list)-1)
    return list


def quickSortHelper(list, first, last):
    if first < last:
        splitPos = partition(list, first, last)
        quickSortHelper(list, first, splitPos-1)
        quickSortHelper(list, splitPos+1, last)


def partition(list, first, last):
    preSplitPos = first
    leftIndex = first+1
    rightIndex = last
    while leftIndex <= rightIndex:
        while leftIndex <= rightIndex and list[leftIndex] <= list[preSplitPos]:
            leftIndex += 1
        while leftIndex <= rightIndex and list[rightIndex] >= list[preSplitPos]:
            rightIndex -= 1
        if leftIndex <= rightIndex:
            list[leftIndex], list[rightIndex] = list[rightIndex], list[leftIndex]
        else:
            
            list[preSplitPos], list[rightIndex] = list[rightIndex], list[preSplitPos]
            preSplitPos = rightIndex
            print(preSplitPos)
            return preSplitPos
        

quickSort(l1)
print(l1)