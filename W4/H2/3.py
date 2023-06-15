# ======= 3 HTML标记匹配 =======
# 实现扩展括号匹配算法，用来检查HTML文档的标记是否匹配。
# HTML标记应该成对、嵌套出现，
# 开标记是<tag>这种形式，闭标记是</tag>这种形式。
#
# 创建一个函数，接受参数为一个字符串，为一个HTML文档中的内容，
# 返回True或False，表示该字符串中的标记是否匹配。
# 输入样例1：
# <html> <head> <title> Example </title> </head> <body> <h1>Hello, world</h1> </body> </html>
# 输出样例1：
# True
# 输入样例2：
# <html> <head> <title> Test </title> </head> <body> <p>It's just a test.</p> <p>And this is for False.<p> </body> </html>
# 输出样例2：
# False
class Stack:
    def __init__(self):
        self.items=[]

    def push(self,value):
        self.items.append(value)
        
    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items==[]

    def size(self):
        return len(self.items)

def HTMLMatch(s) -> bool:
    # 请在此编写你的代码（可删除pass语句）
    s=s.replace(' ','')
    s=s.split('<')
    print(s)
    s1=Stack()
    count=0
    correct=True
    while count<len(s) and correct:
        if '/' in s[count]:
            typ=s[count][1:]
            temp=s1.pop()
            if typ not in temp:
                correct=False
        elif ''==s[count]:
            pass
        else:
            s1.push(s[count])
        count=count+1
    return correct

    


    # 代码结束


# 调用检验
print("======== 3-HTMLMatch ========")
print(
    HTMLMatch(
        "<html> <head> <title>Example</title> </head> <body> <h1>Hello, world</h1> </body> </html>"
    ))
print(
    HTMLMatch(
        "<html> <head> <title> Test </title> </head> <body> <p>It's just a test.</p> <p>And this is for False.<p> </body> </html>"
    ))

