from collections import deque
class Node(object):

    def __init__(self,data):
        self.data = data
        self.nodes = []
        self.visited = False

class Graph(object):

    def __init__(self):
        self.nodes = []


    def displayNodes(self):

        for gn in self.nodes:
            print(gn.data)
            for cn in gn.nodes:
                print(cn.data)



    #With bfs
    def isPath(self,src,dest):
        q = deque()
        for gn in self.nodes:
            if gn.data == src:
                q.append(gn)

                while len(q) > 0:
                    elem = q.popleft()

                    for cn in elem.nodes:
                        if not cn.visited:
                            if cn.data == dest:
                                return True
                            else:
                                 cn.visited = True
                                 print(cn.data)
                                 q.append(cn)

        return False


    #With bfs
    def isPathA(self,src,dest):
        q = deque()
        c = 0

        for gn in self.nodes:
            if src == gn.data:
                q.append(gn)

        while len(q) > 0:
            c+=1
            for qt in q:
                print("##QUE :"+str(qt.data))
            elem = q.popleft()

            for cn in elem.nodes:
                c+=1
                if not cn.visited:
                    if cn.data == dest:
                        print("COUNT IS :" + str(c))
                        return True
                    else:
                        cn.visited = True
                        print(cn.data)
                        q.append(cn)

        print("COUNT IS :"+str(c))
        return False







g = Graph()
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)
n9 = Node(9)
n10 = Node(10)
n11 = Node(11)
n12 = Node(12)
n13 = Node(13)



n1.nodes = [n3,n6]
n2.nodes = [n4]
n3.nodes = [n5,n6]
n4.nodes = [n3,n5]
n5.nodes = [n7]
n6.nodes = [n7,n12]
n7.nodes = [n8,n10]
n8.nodes = [n13]
n10.nodes = [n12]
n12.nodes = [n11]
n13.nodes = [n9]






nodes: Node = [n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13]
g.nodes = nodes
#g.displayNodes()
print(g.isPathA(2,1))
