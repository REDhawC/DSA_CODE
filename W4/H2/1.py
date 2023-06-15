# ======= 1 中缀表达式求值 =======
# 通过把“中缀转后缀”和“后缀求值”两个算法功能集成在一起（非简单的顺序调用），
# 实现对中缀表达式直接求值，新算法还是从左到右扫描中缀表达式，
# 但同时使用两个栈，一个暂存操作符，一个暂存操作数，来进行求值。
#
# 创建一个函数，接受参数为一个字符串，即一个中缀表达式，
# 其中每个数字或符号间由一个空格隔开；
# 返回一个浮点数，即求值的结果。（支持 + - * / ^ 五种运算）
#   其中“ / ”定义为真除True DIV，结果是浮点数类型
# 输入样例1：
# ( 2 + 3 ) * 6 + 4 / 2
# 输出样例1：
# 32.0
# 输入样例2：
# 2 ^ 3 + 4 * 5 - 16 / 2
# 输出样例2：
# 20.0
# 输入样例3：
# ( 5 + 1 ) * 2 / 3 - 3 ^ ( 2 + 8 / 4 ) / 9 + 6
# 输出样例3：
# 1.0
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def calculate(s) -> float:
    # 请在此编写你的代码（可删除pass语句）
    #translate to back-type
    s1=Stack()
    s2=Stack()
    s=s.split(' ')
    l1=[]
    dic1={'*':2,'^':3,'**':3,'/':2,'+':1,'-':1,'(':0}
    t=0
    while t<len(s):
        i=s[t]
        t=t+1
        if i.isdigit():
            l1.append(i)
        elif i in '(':
            s1.push(i)
        elif i in ')':
            while s1.peek()!='(':
                item=s1.pop()
                l1.append(item)
            s1.pop()
        elif i in '+-*/':
            if s1.isEmpty():
                s1.push(i)
            else:
                if dic1[s1.peek()]>=dic1[i]:
                    while dic1[s1.peek()]>=dic1[i]:
                        l1.append(s1.pop())
                        if s1.isEmpty():
                            break
                    s1.push(i)
                else:
                    s1.push(i)
        elif i in '^':
            if s1.isEmpty():
                s1.push('**')
            else:
                if dic1[s1.peek()]>=dic1[i]:
                    while dic1[s1.peek()]>=dic1[i]:
                        l1.append(s1.pop())
                        if s1.isEmpty():
                            break
                    s1.push('**')
                else:
                    s1.push('**')
    while not s1.isEmpty():
        l1.append(s1.pop())
    #calcalation
    for i in l1:
        if i.isdigit():
            s2.push(i)
        else:
            temp=''
            num2=s2.pop()
            num1=s2.pop()
            temp=eval(temp+num1+i+num2)
            print(temp)
            s2.push(str(temp))
    l2=[]
    while not s2.isEmpty():
        tar=float(s2.pop())
        l2.append(tar)
        print(tar)
        
    return ''.join(l1),sum(l2),l2

    # 代码结束


# 调用检验
print("======== 1-calculate ========")
print(calculate("( 2 + 3 ) * 6 + 4 / 2"))
print(calculate("2 ^ 3 + 4 * 5 - 16 / 2"))
print(calculate("( 5 + 1 ) * 2 / 3 - 3 ^ ( 2 + 8 / 4 ) / 9 + 6"))
