class Node:

    # Constructor to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


""" Give a binary search tree and a number,  
inserts a new node with the given number in  
the correct place in the tree. Returns the new  
root pointer which the caller should then use  
(the standard trick to avoid using reference  
parameters). """


def insert(node, data):
    # 1. If the tree is empty, return a new,
    # single node
    if node is None:
        return (Node(data))

    else:
        # 2. Otherwise, recur down the tree
        if data <= node.data:
            node.left = insert(node.left, data)
        else:
            node.right = insert(node.right, data)

            # Return the (unchanged) node pointer
        return node

def display(node):
    if node is None:
        return
    if node.left is not None:
        display(node.left)
    print( node.data)

    if node.right is not None:
        display(node.right)

def inorder(node):
    if node is None:
        return
    else:
        inorder(node.left)
        print(node.data)
        inorder(node.right)


def preOrder(node):

        if node is None:
            return
        else:
            print(node.data)
            preOrder(node.left)
            preOrder(node.right)

def postOrder(node):

        if node is None:
            return
        else:
            postOrder(node.left)
            postOrder(node.right)
            print(node.data)

root = None
root = insert(root,4)
insert(root,2)
insert(root,3)
insert(root,6)

inorder(root)
print("#preorder")
preOrder(root)
print("#postorder")
postOrder(root)