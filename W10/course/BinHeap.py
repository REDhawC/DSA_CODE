class BinHeap:
    def __init__(self):
        self.heapList = [0]  # 0用于占位
        self.currentSize = 0

    def percUp(self, i):
        while i // 2 > 0:  # 父节点非占位0时,
            # 如果当前的
            if self.heapList[i] < self.heapList[i // 2]:
                temp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = temp
            i = i // 2  # 更新位置,继续比较更上面的父节点

    def insert(self, k):
        self.heapList.append(k)  # 先从列表尾部进入
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)  # 然后再去比较,上升
        # 特点: heapList[1]是最小值

    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            minChildIndex = self.getMinChild(i)
            if self.heapList[i] > self.heapList[minChildIndex]:
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[minChildIndex]
                self.heapList[minChildIndex] = temp
                i = minChildIndex
            i = minChildIndex

    def getMinChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2 + 1] > self.heapList[i * 2]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        delVal = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.heapList.pop()
        self.currentSize -= 1
        self.percDown(1)
        return delVal


heap = BinHeap()
heap.insert(2)
heap.insert(1)
heap.insert(11)
# heap.insert(0.5)
print(heap.heapList)
print(heap.height())
