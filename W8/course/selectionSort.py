l1=[1,2,3,4,66,23,11]

def selectionSort(list):
    for num in range(len(list)-1,0,-1):
        # 从列表长度-1开始,每次循环递减1,到1结束 [*左闭右开,0取不到]
        maxPosition=0
        for i in range(1,num+1):
            if list[i]>list[maxPosition]:
                maxPosition=i
                # 记录最大值的位置
        list[num],list[maxPosition]=list[maxPosition],list[num]
        # 最大值的数 与 list末尾数 换位
    return list

selectionSort(l1)