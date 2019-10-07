#### solution 3.2 : Return the minimum element of the stack
class MyStack:


    def __init__(self):
        self.items = []
        self.top = None
        self.min = None

    def push(self, _item):

        if self.min is None:
            self.min = _item

        if _item < self.min:
            self.min = _item

        self.items.append(_item)
        self.top = _item

    def returnMin(self):
        return self.min

    def isEmpty(self):
        return self.items == []

    def peek(self):
        return self.top

## Solution 3.1
class StackM:

    def __init__(self, _div, _items):
        self.items = _items
        self.top = None
        self.tail = None
        self._div = _div
        self.partition = self.checkpartition()

    def checkpartition(self):
        _size = len(self.items) / self._div

        if _size != 0:
            print("Size is "+ str(_size))










e = [1,2,3,4,5,6,7,8,9]
m  = StackM(3, e)
