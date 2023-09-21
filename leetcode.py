class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def inOrderTraversal(self, root):
        if root:
            self.inOrderTraversal(root.left)

            print(root.data, end="->")

            self.inOrderTraversal(root.right)

    def createList(self, root, output=[]):
        if root:
            self.createList(root.left, output)
            # output += [root.data]
            output.append(root.data)
            self.createList(root.right, output)

        return output

    # not recursive way
    def addNode(self, root):
        if root is None:
            return []
        return self.addNode(root.left) + [root.data] + self.addNode(root.right)


# preOrder
def preOrder(root):
    if root:
        # print val of root
        print(root.data, end="->")

        # then go to the left child
        preOrder(root.left)

        # finally go to right child
        preOrder(root.right)


# inOrder
def inOrder(root):
    if root:
        # prints the value of left first
        inOrder(root.left)
        print(root.data, end="->")

        # finally go to the right
        inOrder(root.right)


# postOrder
def postOrder(root):
    if root:
        # prints bottom rows first
        postOrder(root.left)
        postOrder(root.right)

        # finally print root
        print(root.data, end="->")


# create an object
# root = Node(1)
# root.right = Node(2)
# root.right.left = Node(3)

# example from book
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# print preOrder
print("preOrder traversal")
preOrder(root)
print("\n")
print("inOrder traversal")
inOrder(root)
print("\n")
print("postOrder traversal")
postOrder(root)

# print("\n")
# print("Testing object method:")
# print(root.inOrderTraversal(root))

print("\n")
print("Returned as an array: ")
print(root.createList(root))

print("\n")
print("Non-recursive way")
print(root.addNode(root))
