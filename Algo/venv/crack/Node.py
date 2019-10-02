class Node(object):

    def __init__(self):
        self.next = None
        self.data = None

    def addNode(self, end):
        n = self
        while n.next is not None:
            n = n.next
        n.next = end

    def printAllNodes(self):

        node = self
        while node is not None:
            print(node.data)
            node = node.next

    def deleteNode(self, node):

        _head = self
        current = self
        prev = None
        _found = False

        while not _found:
            if current.data == node.data:
                _found = True
                break
            else:
                prev = current
                current = current.next

        if prev is None:
            _head = current
        else:
            prev.next = current.next

    def searchNode(self,node):
        _current = self
        _found = False

        while not _found and _current is not None:
            if _current.data == node.data:
                _found = True
                break
            else:
                _current = _current.next
        return  _found

## Delete duplicates from the linked list
    def delete_duplicate(self):
        x = set()
        _current = self
        while _current.next is not None:
            if _current.data in x:
                x.remove(_current.data)
                self.deleteNode(_current)
            else:
                x.add(_current.data)
                _current = _current.next


######################################Find Kth element from last from Linked List

    def findFromLast(self,node,k,_counter):

        if node is None:
            return
        head = node
        tail = node.next
        _counter += 1
        self.findFromLast(tail,k,_counter)
        if _counter == k:
           print(head.data)
########################################


n1 = Node()
n2 = Node()
n3 = Node()
n4 = Node()
n5 = Node()
n6 = Node()

n6.data = 666
n5.data = 122
n4.data = 444
n3.data = 133
n2.data = 122
n1.data = 111


n1.addNode(n2)
n1.addNode(n3)
n1.addNode(n4)
n1.addNode(n5)
n1.addNode(n6)
####################################
n1.deleteNode(n3)
n1.printAllNodes()
print("++++++++++++++++++++++++++++++")
n1.delete_duplicate()
n1.printAllNodes()

##########################
print("################################")
n1.findFromLast(n1,1,0)

