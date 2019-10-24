class GNode(object):

    def __init__(self,data):
        self.data = data
        self.nodes = []

class Graph(object):

    def __init__(self):
        self.nodes = []

    def displayNodes(self, gnode):

        for gn in gnode.nodes:
            for cn in gn.nodes:
                print(cn.data)
                print(gn.data)



g = Graph()
n1 = GNode(1)
n2 = GNode(2)
n3 = GNode(3)
a1 = GNode(4)
a2 = GNode(5)
a3 = GNode(7)



a2.nodes.append(a3)
n2.nodes.append(a2)
n1.nodes.append(a1)
n1.nodes.append(n2)

g.nodes.append(n1)




## Display Graph Nodes
g.displayNodes(g)