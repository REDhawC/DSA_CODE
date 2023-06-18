class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()  # use Node's __iter__()

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size = self.size + 1

    def _put(self, key, val, currentNode):
        # obey the rule of SMALLER-LEFT,BIGGER-RIGHT
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
        if key > currentNode.key:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)

    def __setitem__(self, key, value):
        # e.g. tree[1]='dick'
        self.put(key, value)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, currentNode):
        if not currentNode:  # cannot find anything by looping children
            # and return None
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)

    def __getitem__(self, key):  # print(tree[6])-> dick
        return self.get(key)

    def __contains__(self, key):  # 'dick' in Tree -> True/False
        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            targetNode = self._get(key, self.root)
            if targetNode:
                self.remove(targetNode)
                self.size -= 1
            else:
                raise KeyError("Error, incorrect key")
        else:
            if self.root.key == key and self.size == 1:
                self.root = None
                self.size -= 1
            else:
                raise KeyError("Error, incorrect key")

    def __delitem__(self, key):
        self.delete(key)

    def remove(self, node):
        # 1.leftNode
        if not node.hasAnyChild():
            if node == node.parent.leftChild:
                node.parent.leftChild = None
            else:
                node.parent.rightChild = None
        # 2. targetNode has one child
        elif node.hasAnyChild() and (not node.hasBothChild()):
            if node.hasLeftChild():
                if node.isLeftChild():
                    # a.LEFT -> LEFT
                    node.leftChild.parent = node.parent
                    node.parent.leftChild = node.leftChild
                elif node.isRightChild():
                    # b.LEFT -> RIGHT
                    node.leftChild.parent = node.parent
                    node.parent.rightChild = node.leftChild
                else:
                    # c.ROOT
                    node.replaceNodeData(
                        node.leftChild.key,
                        node.leftChild.payload,
                        node.leftChild.leftChild,
                        node.leftChild.rightChild,
                    )
            else:
                if node.isLeftChild():
                    # a.RIGHT -> LEFT
                    node.rightChild.parent = node.parent
                    node.parent.leftChild = node.rightChild
                elif node.isRightChild():
                    # b.RIGHT -> RIGHT
                    node.rightChild.parent = node.parent
                    node.parent.rightChild = node.rightChild
                else:
                    # c.ROOT
                    node.replaceNodeData(
                        node.rightChild.key,
                        node.rightChild.payload,
                        node.rightChild.leftChild,
                        node.rightChild.rightChild,
                    )
        elif node.hasBothChild():  # 3.has two children
            succ = node.findSuccessor()  # we got to find a proper node
            succ.spliceOut()  # to replace the romoved one
            node.key = succ.key
            node.payload = succ.payload


class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
        self.balanceFactor = self.balanceFactor()

    def balanceFactor(self):
        leftHeight = 0
        rightHeight = 0
        if self.hasLeftChild():
            leftHeight = self.leftChild.getHeight()
        if self.hasRightChild():
            rightHeight = self.rightChild.getHeight()
        return leftHeight - rightHeight

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and (self.parent.leftChild == self)

    def isRightChild(self):
        return self.parent and (self.parent.rightChild == self)

    def isRoot(self):
        return not self.parent

    def hasAnyChild(self):
        return self.leftChild or self.rightChild

    def hasBothChild(self):
        return self.leftChild and self.rightChild

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    def __iter__(self):
        if self:
            if self.hasLeftChild():
                for element in self.leftChild:
                    # 这里的for循环实际上再次调用了__iter__
                    # 形成了递归调用
                    yield element
            # yield 语句会将当前状态保存下来，并返回一个元素给调用者。
            # 当下一次迭代时，会从上一次的状态继续执行，直到遍历完所有元素。
            yield self.key
            if self.hasRightChild():
                for element in self.rightChild:
                    yield element

    def findSuccessor(self):  # look for the smallest node among rightchild's leftchilds
        succ = self.rightChild.findMin()
        return succ

    def findMin(self):
        currentNode = self
        while currentNode.hasRightChild():
            currentNode = currentNode.leftChild
        return currentNode

    def spliceOut(self):
        if not self.hasAnyChild():
            if self.isLeftChild():
                self.parent.leftChild = None
        elif self.hasAnyChild():
            self.parent.leftChild = self.rightChild
            self.rightChild.parent = self.parent

    def getHeight(self):
        if self.leftChild and self.rightChild:
            return 1 + max(self.leftChild.getHeight(), self.rightChild.getHeight())
        elif self.leftChild:
            return 1 + self.leftChild.getHeight()
        elif self.rightChild:
            return 1 + self.rightChild.getHeight()
        else:
            return 1


class AVLTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()  # use Node's __iter__()

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size = self.size + 1

    # the only difference between AVLtree and BST is
    # the _put method
    def _put(self, key, val, currentNode):
        # obey the rule of SMALLER-LEFT,BIGGER-RIGHT
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
                self.updateBalance(currentNode.leftChild)
        if key > currentNode.key:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)
                self.updateBalance(currentNode.rightChild)

    def updateBalance(self, node):
        if node.balanceFactor < -1 or node.balanceFactor > 1:
            self.rebalance(node)
        if node.parent != None:
            if node.isLeftChild():
                node.parent.balanceFactor += 1
            elif node.isRightChild():
                node.parent.balanceFactor -= 1
            if node.parent.balanceFactor != 0:
                self.updateBalance(node.parent)

    def rotateLeft(self, rotRoot):
        newRoot = rotRoot.rightChild
        rotRoot.rightChild = newRoot.leftChild
        if newRoot.leftChild != None:
            newRoot.leftChild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild = newRoot
            else:
                rotRoot.parent.rightChild = newRoot
        newRoot.leftChild = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balanceFactor = (
            rotRoot.balanceFactor + 1 - min(newRoot.balanceFactor, 0)
        )
        newRoot.balanceFactor = (
            newRoot.balanceFactor + 1 - min(rotRoot.balanceFactor, 0)
        )

    def rotateRight(self, rotRoot):
        newRoot = rotRoot.leftChild
        rotRoot.leftChild = newRoot.rightChild
        if newRoot.rightChild != None:
            newRoot.rightChild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild = newRoot
            else:
                rotRoot.parent.rightChild = newRoot
        newRoot.rightChild = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balanceFactor = (
            rotRoot.balanceFactor - 1 - max(newRoot.balanceFactor, 0)
        )
        newRoot.balanceFactor = (
            newRoot.balanceFactor - 1 - max(rotRoot.balanceFactor, 0)
        )

    def rebalance(self, node):
        if node.balanceFactor < 0:
            if node.rightChild.balanceFactor > 0:
                self.rotateRight(node.rightChild)
                self.rotateLeft(node)
            else:
                self.rotateLeft(node)
        elif node.balanceFactor > 0:
            if node.leftChild.balanceFactor < 0:
                self.rotateLeft(node.leftChild)
                self.rotateRight(node)
            else:
                self.rotateRight(node)

    def __setitem__(self, key, value):
        # e.g. tree[1]='dick'
        self.put(key, value)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, currentNode):
        if not currentNode:  # cannot find anything by looping children
            # and return None
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)

    def __getitem__(self, key):  # print(tree[6])-> dick
        return self.get(key)

    def __contains__(self, key):  # 'dick' in Tree -> True/False
        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            targetNode = self._get(key, self.root)
            if targetNode:
                self.remove(targetNode)
                self.size -= 1
            else:
                raise KeyError("Error, incorrect key")
        else:
            if self.root.key == key and self.size == 1:
                self.root = None
                self.size -= 1
            else:
                raise KeyError("Error, incorrect key")

    def __delitem__(self, key):
        self.delete(key)

    def remove(self, node):
        # 1.leftNode
        if not node.hasAnyChild():
            if node == node.parent.leftChild:
                node.parent.leftChild = None
            else:
                node.parent.rightChild = None
        # 2. targetNode has one child
        elif node.hasAnyChild() and (not node.hasBothChild()):
            if node.hasLeftChild():
                if node.isLeftChild():
                    # a.LEFT -> LEFT
                    node.leftChild.parent = node.parent
                    node.parent.leftChild = node.leftChild
                elif node.isRightChild():
                    # b.LEFT -> RIGHT
                    node.leftChild.parent = node.parent
                    node.parent.rightChild = node.leftChild
                else:
                    # c.ROOT
                    node.replaceNodeData(
                        node.leftChild.key,
                        node.leftChild.payload,
                        node.leftChild.leftChild,
                        node.leftChild.rightChild,
                    )
            else:
                if node.isLeftChild():
                    # a.RIGHT -> LEFT
                    node.rightChild.parent = node.parent
                    node.parent.leftChild = node.rightChild
                elif node.isRightChild():
                    # b.RIGHT -> RIGHT
                    node.rightChild.parent = node.parent
                    node.parent.rightChild = node.rightChild
                else:
                    # c.ROOT
                    node.replaceNodeData(
                        node.rightChild.key,
                        node.rightChild.payload,
                        node.rightChild.leftChild,
                        node.rightChild.rightChild,
                    )
        elif node.hasBothChild():  # 3.has two children
            succ = node.findSuccessor()  # we got to find a proper node
            succ.spliceOut()  # to replace the romoved one
            node.key = succ.key
            node.payload = succ.payload


tree = AVLTree()
tree.put(2, "HAO")
tree.put(1, "YY")
# tree.delete(1)
# tree.delete(2)
print(tree[2], tree[1], tree.size, tree.root.balanceFactor)
