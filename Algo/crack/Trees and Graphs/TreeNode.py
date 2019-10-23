from collections import deque
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

    def preOrder(self, node):
        if node is None:
            return
        else:
            print(node.data)
            self.preOrder(node.left)
            self.preOrder(node.right)

    def postOrder(self, node):

        if node is None:
            return
        else:
            self.postOrder(node.left)
            self.postOrder(node.right)
            print(node.data)

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


    def findMin(self,root):
        if root is None:
            return
        else:
            while root.left is not None:
                root = root.left
            return root

    def findHeight(self,root):

        if root is None:
            return -1

        hleft = self.findHeight(root.left)
        hright = self.findHeight(root.right)

        return max(hleft, hright) + 1

    que = deque()
    def bfs(self, root):

        if root is None:
            return

        if root.left is not None:
            self.que.append(root.left)
        if root.right is not None:
            self.que.append(root.right)

        print(root.data)

        if len(self.que) == 0:
            return

        self.bfs(deque.popleft(self.que))


    def isBST(self, node, prev):
        if node is None:
            return
        else:
            self.isBST(node.left, prev)

            print(prev)
            if node.data < prev.index(1):
                return False
            else:
                prev.append(node.data)

            self.isBST(node.right, prev)

        return True




n = Node(9)
t = Tree()
t.insertNode(n,7)
t.insertNode(n,12)
t.insertNode(n,4)
t.insertNode(n,8)
t.insertNode(n,10)

t.insertNode(n,14)
t.insertNode(n,3)
t.insertNode(n,5)
t.insertNode(n,6)
t.insertNode(n,11)
t.insertNode(n,13)
t.insertNode(n,15)


t.inOrder(n)



print("##################")
nodep = t.deleteNode(n,20)

t.inOrder(n)


print("##################After inserting 20 again")
t.insertNode(n,20)



t.inOrder(n)


print("################# Find Min in Binary Tree:")

print(t.findMin(n).data)

print("###### Find Height of bst")
print(t.findHeight(n))

print("####Implement bfs")
t.bfs(n)

print("## preOrder")
t.preOrder(n)

print("############## POSt ORder traversal")
t.postOrder(n)


p = Node(6)
q = Node(7)
r = Node(8)
p.right = r
p.left = q

print("###### is BST ")
x = [9]
print(t.isBST(p,x))

print("### inorder again #####")
print(t.inOrder(p))


