import sys

sys.path.append("C:/Users/redhawc/Desktop/DSA_CODE/pythonds")
from BinaryTree_Node import BinaryTree
from stack import Stack

exp = "( 1 - 2 ) * ( 3 + 7 )"


def parseTree(expression):
    expression = expression.split(" ")
    stack = Stack()
    tree = BinaryTree("")
    stack.push(tree)  # set a upper-level tree in case of going up later
    curTree = BinaryTree("")
    for i in expression:
        print("exp", i)
        if i in "(":
            curTree.insertLeft("")
            stack.push(curTree)  # go down to lower level
            curTree = curTree.leftChild
            print("val:", curTree.root)
            print("left:", curTree.getLeftChildVal())
        elif i not in "+-*/()":
            curTree.setRootVal(int(i))
            print(curTree.root)
            print("left:", curTree.getLeftChildVal())
            print("right:", curTree.getRightChildVal())
            parent = stack.pop()
            # if parent.leftChild and parent.leftChild != "":
            #     parent.rightChild = curTree
            # else:
            #     parent.leftChild = curTree
            curTree = parent
        elif i in "+-*/":
            curTree.setRootVal(i)
            print(curTree.root)
            curTree.insertRight("")
            print("left:", curTree.getLeftChildVal())
            stack.push(curTree)  # go down to lower level
            curTree = curTree.rightChild
        elif i in ")":
            curTree = stack.pop()
            print(curTree.root)
            print("left:", curTree.getLeftChildVal())
        print("--------")
    return tree


def buildParseTree(expression):
    # 将表达式字符串按照空格分隔成操作数和运算符的列表
    expression = expression.split(" ")

    # 创建一个空的二叉树对象，并将其作为根节点存储在栈中
    stack = Stack()
    tree = BinaryTree("")
    stack.push(tree)
    currentTree = tree

    # 遍历表达式中的每个操作数和运算符
    for item in expression:
        if item == "(":
            # 如果当前字符是左括号，创建一个空的左子树，并将其设置为当前节点的左子节点
            currentTree.insertLeft("")
            stack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif item in ["+", "-", "*", "/"]:
            # 如果当前字符是一个运算符，将其作为当前节点的值，并创建一个空的右子树
            currentTree.setRootVal(item)
            currentTree.insertRight("")
            # 将当前节点入栈，将右子树设置为当前节点，并继续向下遍历
            stack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif item == ")":
            # 如果当前字符是右括号，弹出栈，将当前节点设置为父节点，并继续向上遍历
            currentTree = stack.pop()
        else:
            try:
                # 如果当前字符是数字，则将其作为当前节点的值
                currentTree.setRootVal(int(item))
                # 弹出栈，将当前节点设置为父节点，并继续向上遍历
                parent = stack.pop()
                currentTree = parent
            except ValueError:
                raise ValueError("Token '{}' is not a valid integer".format(item))

    return tree


import operator


def calTree(tree):
    operations = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }
    if (not tree.leftChild) and (not tree.rightChild):
        return tree.getRootVal()
    else:
        return operations[tree.getRootVal()](
            calTree(tree.leftChild), calTree(tree.rightChild)
        )


def printexp(tree):
    sVal = ""
    if tree:
        sVal = " " + printexp(tree.getLeftChild())
        sVal = sVal + str(tree.getRootVal())
        sVal = sVal + printexp(tree.getRightChild()) + " "
    return sVal


# test = parseTree(exp)
exp1 = "( 1 + 2 ) * ( 3 - 7 )"
test1 = buildParseTree(exp1)
test1.preOrder()
print("--------------------")
test1.inOrder()
print("--------------------")
test1.postOrder()
print("--------------------")
print(printexp(test1))
print("--------------------")
print(test1.getRootVal())
print(test1.getLeftChildVal())
print(test1.getRightChildVal())
print(test1)
# print(test.leftChild.getLeftChildVal())
# print(test.leftChild.getRightChildVal())
# print(test.rightChild.getLeftChildVal())
# print(test.rightChild.getRightChildVal())
# print(test.rightChild.getLeftChildVal())
# calTree(buildParseTree(exp))
