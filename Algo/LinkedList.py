class Node(object):
    def __init__(self, initdata):
        self.next = None
        self.data = initdata

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newData):
        self.data = newData

    def setNext(self, newnext):
        self.next = newnext

class LinkedList(object):

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return  self.head == None

    def addNode(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def searchNode(self,item):
        current = self.head
        found = False

        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def deleteNode(self,item):
        current = self.head
        previous = None
        found = False

        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head  = current.getNext()
        else:
            previous.setNext(current.getNext())



