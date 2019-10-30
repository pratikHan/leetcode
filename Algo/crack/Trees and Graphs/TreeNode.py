from collections import deque

class LNode(object):

    def __init__(self, data):
        self.data = data
        self.next = None

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
            return Node(data)
        else:
            if data < node.data:
                node.left = self.insertNode(node.left, data)

            else:
                node.right = self.insertNode(node.right, data)

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
            return None
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


    def deleteNodeA(self, node, data):

        if node is None:
            return node
        elif data < node.data:
            node.left = self.deleteNodeA(node.left, data)
        elif data > node.data:
            node.right = self.deleteNodeA(node.right,data)
        else:
            ## case 1
            if node.left is None and node.right is None:
                return None

            elif node.left is None:
                temp = node.right
                return temp

            elif node.right is None:
                temp = node.left
                return temp

            else:
                ## case 2 Childrens
                temp = self.findMin(node.right)
                node.right = self.deleteNodeA(node.right, temp.data)

        return node



    def createBSTMinH(self,list,start,end):

        if (start > end):
            return None

        mid = (start + end)//2


        root = Node(list[mid])

        root.left = self.createBSTMinH(list,start,mid-1)

        root.right = self.createBSTMinH(list,mid + 1, end)

        return root

    ds = [None,None,None]

    def ListinTrees(self,node,height):
        """ Design a Tree such that at every depth
            d you create d Linked Lists
        """
        if self.ds[height] is None:
            self.ds[height] = LNode(node)
        else:
            temp = self.ds[height]
            inserted = False

            while temp is not None and not inserted:
                if temp.next is None:
                    temp.next = LNode(node)
                    inserted = True
                else:
                    temp = temp.next







    def testRec(self,root,h):

        if root is None:
            return

        else:
            h += 1
            self.testRec(root.left,h)
            self.testRec(root.right,h)
            print(" #Height is   " + str(h) + "  Data is  " + str(root.data))
            self.ListinTrees(root.data,h)





"""

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

print(t.findHeight(n))




t.inOrder(n)

t.deleteNode(n,10)

print("#### After Deleteing node ")
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
"""

n = [1,2,3,4,5,6,7]
t = Tree()
temp = t.createBSTMinH(n,0,len(n)-1)
#t.postOrder(temp)

t.testRec(temp,-1)





print("###### TEst with lists")
