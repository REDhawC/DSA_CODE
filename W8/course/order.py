def sequentialSearch(list, item):
    pos = 0
    found = False
    while not found and pos < len(list):
        if list[pos] == item:
            found = True
        pos += 1
    return found


def orderedSequentialSearch(list, item):
    pos = 0
    found = False
    while not found and pos < len(list):
        if list[pos] == item:
            found = True
        elif list[pos] > item:
            return False
        pos += 1
    return found


def binarySearch(list, item):
    first = 0
    last = len(list)-1
    found = False
    while not found and first <= last:
        midPoint = (first+last)//2
        if list[midPoint] == item:
            found = True
        else:
            if item < list[midPoint]:
                last = midPoint-1
            else:
                first = midPoint+1
    return found

def recursionBinarySearch(list, item):
    # print(list)
    
    if len(list)==0:
        print('fail!')
    else:
        print(list)
        midPoint=len(list)//2
        print(list[midPoint])
        if list[midPoint]==item:
            print('found!')
        else:
            if list[midPoint]>item:
            
                recursionBinarySearch(list[:midPoint],item)
            else:
                recursionBinarySearch(list[midPoint+1:],item)

recursionBinarySearch([1,2,3,4],1)
print('-----------------')
recursionBinarySearch([1,2,3,4],2)
print('-----------------')
recursionBinarySearch([1,2,3,4],3)
print('-----------------')
recursionBinarySearch([1,2,3,4],4)
print('-----------------')
recursionBinarySearch([1,2,3,4],5)

# def recursionBinarySearch(list, item):
#     # print(list)
    
#     if len(list)==0:
#         return False
#     else:
#         midPoint=len(list)//2
#         if list[midPoint]==item:
#             return True
#         elif list[midPoint]>item:
            
#             recursionBinarySearch(list[:midPoint],item)
#         else:
#             recursionBinarySearch(list[midPoint+1:],item)
