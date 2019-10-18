class Node(object):

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

class Tree(object):

    def __init__(self):
        self.root = None

    def insertNode(self,node,data):

        if self.root is None:
            self.root = node

        if node is None:
            return (Node(data))
        else:
            if data < node.data:
                node.left = self.insertNode(node.left,data)

            else:
                node.right = self.insertNode(node.right,data)

        if node.left is not None:
            node.left.parent = node

        if node.right is not None:
            node.right.parent = node

        return node

    def searchNode(self, node, data):

        if node is None:
            return

        if node.data == data:
            return node

        if data < node.data:
           return self.searchNode(node.left,data)
        else:
            return self.searchNode(node.right,data)

    def deleteNode(self,node,data):

        if node is None:
            return None

        nodex = self.searchNode(node, data)

        if nodex is not None:

            if nodex.left is None and nodex.right is None:
                if nodex.parent.left is nodex: nodex.parent.left = None
                else:
                    nodex.parent.right = None

            if nodex.left is not None and nodex.right is None:
                nodex.parent.right = nodex.left
                nodex.left.parent = nodex.parent
                return nodex

            if nodex.right is not None and nodex.left is None:
                nodex.parent.left = nodex.right
                nodex.right.parent = nodex.parent
                return nodex



    def inOrder(self,node):
        if (node is None):
            return
        else:
            self.inOrder(node.left)
            print(node.data)
            self.inOrder(node.right)


##Wron Logic
    def isBinarySearchTree(self, node):


        if node.parent is None:
            self.isBinarySearchTree(node.left)
            self.isBinarySearchTree(node.right)

        if node is None:
            return True


        if node.left is not None and node.left.data <= node.data:
            self.isBinarySearchTree(node.left)
        else:
            return False

        if node.right is not None and node.right.data > node.data:
            self.isBinarySearchTree(node.right)
        else:
            return False

        return True




n = Node(8)
t = Tree()
t.insertNode(n,20)
t.insertNode(n,4)
t.insertNode(n,7)
t.insertNode(n,3)
t.insertNode(n,12)

t.insertNode(n,16)
t.insertNode(n,6)

t.inOrder(n)



print("##################")
nodep = t.deleteNode(n,20)

t.inOrder(n)


print("##################After inserting 20 again")
t.insertNode(n,20)



t.inOrder(n)


print("################# IS Binary treee:")

print(t.isBinarySearchTree(p))




