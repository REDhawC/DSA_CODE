class BinaryTree:
    # This is a node, not a full tree with branches.
    def __init__(self, root):
        self.root = root
        self.leftChild = None
        self.rightChild = None

    def getRootVal(self):
        return self.root

    def insertLeft(self, newNodeVal):
        if self.leftChild != None:
            newLeft = BinaryTree(newNodeVal)
            newLeft.leftChild = self.leftChild
            self.leftChild = newLeft
        else:
            self.leftChild = BinaryTree(newNodeVal)

    def insertRight(self, newNodeVal):
        if self.rightChild != None:
            newRight = BinaryTree(newNodeVal)
            newRight.rightChild = self.rightChild
            self.rightChild = newRight
        else:
            self.rightChild = BinaryTree(newNodeVal)

    def setRootVal(self, val):
        self.root = val

    def getLeftChild(self):
        return self.leftChild

    def getLeftChildVal(self):
        if self.leftChild:
            return self.leftChild.root
        else:
            return "None"

    def getRightChild(self):
        return self.rightChild

    def getRightChildVal(self):
        if self.rightChild:
            return self.rightChild.root
        else:
            return "None"

    def preOrder(self):
        print(self.root)
        if self.leftChild:
            self.leftChild.preOrder()
        if self.rightChild:
            self.rightChild.preOrder()

    def inOrder(self):
        if self.leftChild:
            self.leftChild.inOrder()
        print(self.root)
        if self.rightChild:
            self.rightChild.inOrder()

    def postOrder(self):
        if self.leftChild:
            self.leftChild.inOrder()
        if self.rightChild:
            self.rightChild.inOrder()
        print(self.root)
