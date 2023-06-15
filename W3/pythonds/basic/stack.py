# Bradley N. Miller, David L. Ranum
# Introduction to Data Structures and Algorithms in Python
# Copyright 2005
# 
#stack.py

class Stack(list):
    def push(self, item):
        self.append(item)

    def peek(self):
        return self[-1]

    def isEmpty(self):
        return self == []

    def size(self):
        return len(self)

    def __repr__(self):
        l = len(self) * 7
        s = "|" + "-" * l + ")\n|"
        for a in self:
            s += "| %-5s" % a
        s += "\n|" + "-" * l + ")"
        return s

    __str__ = __repr__
