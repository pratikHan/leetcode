class Myqueue(object):



    def __init__(self,len):
        self.front = None
        self.rear = None
        self.length = len

    def enQue(self, x):


        newnode = Node(x)

        if self.front is None:
            self.front = self.rear = newnode

        else:
            self.rear.next = newnode
            self.rear = newnode


    def deQue(self):
        if self.front is None:
            return
        elif self.front == self.rear:
            self.front = self.rear = None
            self.length -= 1
        else:
            self.front = self.front.next
            self.length -= 1

    def sizer(self):
        return self.length





class Node(object):

    def __init__(self,data):
        self.data = data
        self.next = None



'''def printQ(queue):

    if queue is None:
        return
    else:
        temp = queue.front
        if temp is None:
            print("Temp is none")
        while temp is not None:
            print(temp.data)
            temp = temp.next
            print("Len is "+str(queue.length))

'''


class MyStackX(object):

    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop(0)
    def peek(self):
        return self.items[0]

    def printq(self):
        c = 0
        for e in self.items:
            print(e)

    def isEmpty(self):
        if len(self.items) >= 1:
            return False
        else:
            return True

class MQueue(object):

    def __init__(self):
        self.stackNew = MyStackX()
        self.stackOld = MyStackX()

    def enqueue(self,item):
        self.stackNew.push(item)

    def shiftStacks(self):

        if self.stackOld.isEmpty():
            print("is old is Empty")
            while not self.stackNew.isEmpty():
                print("NEw is not empty")
                self.stackOld.push(self.stackNew.pop())

    def peek(self):
        self.shiftStacks()
        return self.stackOld.peek()

    def deque(self):
        self.shiftStacks()
        return self.stackOld.pop()

    def printQ(self):
        print("Stack New")
        self.stackNew.printq()
        print("Stack Old")
        self.stackOld.printq()



print("###### Queue")

q = MQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

q.printQ()

print("##### ")
print(q.peek())
q.printQ()









'''q = Myqueue(5)
q.enQue(1)
q.enQue(2)
q.enQue(3)
q.enQue(4)
q.enQue(5)
q.deQue()

printQ(q)'''


