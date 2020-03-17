class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left == None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = Node(value)
            else:
                self.right.insert(value)
    
    def printSelf(self):
        if self.left == None:
            print(self.value)
        else:
            self.left.printSelf()
            print(self.value)

        if self.right != None:
            self.right.printSelf()
        else:
            pass

class BinaryTree:
    def __init__(self, value: int):
        self.root = Node(value)

    def insert(self, value):
        self.root.insert(value)

    def tranverse(self):
        self.root.printSelf()

# Initialization of the Binary Tree
binary_tree = BinaryTree(5)

# Test random values
binary_tree.insert(7)
binary_tree.insert(8)
binary_tree.insert(2)
binary_tree.insert(3)
binary_tree.insert(10)
binary_tree.insert(1)
binary_tree.insert(0)

# Tranverse tree
binary_tree.tranverse()
