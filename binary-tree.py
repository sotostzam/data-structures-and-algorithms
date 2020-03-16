class Tree:
    def __init__(self):
        self.root = None
        self.left = None
        self.right = None

    def addNode(self, node):
        if self.root == None:
            self.root = node
        else:
            if node.value < self.root.value:
                if self.left == None:
                    self.left = node
                else:
                    self.left = self.addNode(node)
            else:
                if self.right == None:
                    self.right = node
                else:
                    self.right = self.addNode(node)
    
        print("New node: ")
        print(self.root)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Initialization of the Binary Tree
binary_tree = Tree()

binary_tree.addNode(Node(4))
binary_tree.addNode(Node(5))
binary_tree.addNode(Node(3))
