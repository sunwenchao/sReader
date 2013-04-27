# coding=utf-8


class Stack():

    def __init__(self):
        self.dataList = []
        self._aaa = 1

    def get(self):
        if len(self.dataList) == 0:
            return None
        return self.dataList.pop()

    def add(self, o):
        self.dataList.append(o)

    @property
    def egg(self):
        return self._aaa

s = Stack()

# s.add(1)
# s.add(2)
# print s.get()
# print s.get()
# print s.get()
print s.egg
s.egg = 2
print s.egg
