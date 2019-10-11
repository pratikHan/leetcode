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







class Node(object):

    def __init__(self,data):
        self.data = data
        self.next = None



def printQ(queue):

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




q = Myqueue(5)
q.enQue(1)
q.enQue(2)
q.enQue(3)
q.enQue(4)
q.enQue(5)
q.deQue()

printQ(q)

