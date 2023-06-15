def BinaryTree(rootValue):
    return [rootValue, [], []]


def insertLeft(root, newBranch):
    leftElement = root.pop(1)
    if len(leftElement) != 0:
        root.insert(1, [newBranch, leftElement, []])
    else:
        root.insert(1, [newBranch, [], []])


def insertRight(root, newBranch):
    rightElement = root.pop(2)
    if len(rightElement) != 0:
        root.insert(2, [newBranch, [], rightElement])
    else:
        root.insert(2, [newBranch, [], []])


def getRootVal(tree):
    return tree[0]


def setRootVal(tree, val):
    tree[0] = val


def getLeftChild(tree):
    return tree[1]


def getRightChild(tree):
    return tree[2]
