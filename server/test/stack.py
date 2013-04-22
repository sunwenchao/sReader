# coding=utf-8


class Stack():

    def __init__(self):
        self.dataList = []

    def get(self):
        if len(self.dataList) == 0:
            return None
        return self.dataList.pop()

    def add(self, o):
        self.dataList.append(o)

s = Stack()

s.add(1)
s.add(2)
print s.get()
print s.get()
print s.get()
