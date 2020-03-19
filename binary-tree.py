class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, value):
        self.root = Node(value)

    def tranverseNLR(self, node, order = ''):
        order += str(node.value) + ", "
        if node.left != None:
            order += self.tranverseNLR(node.left)   
        if node.right != None:
            order += self.tranverseNLR(node.right)
        return order

    def tranverseLNR(self, node, order = ''):
        if node.left == None:
            order += str(node.value) + ", "
        else:
            order += self.tranverseLNR(node.left)
            order += str(node.value) + ", "
        if node.right != None:
            order += self.tranverseLNR(node.right)
        return order

    def tranverseLRN(self, node, order = ''):
        if node.left != None:
            order += self.tranverseLRN(node.left)
        if node.right != None:
            order += self.tranverseLRN(node.right)
        order += str(node.value) + ", "
        return order

    def tranverse_level_order(self, node):
        bfsList = []
        bfsList.append(node)
        order = ''
        while len(bfsList) != 0:
            if bfsList[0].left == None and bfsList[0].right == None:
                order += str(bfsList[0].value) + ", "
                bfsList.pop(0)
            else:
                if bfsList[0].left != None:
                    bfsList.append(bfsList[0].left)
                if bfsList[0].right != None:
                    bfsList.append(bfsList[0].right)
                order += str(bfsList[0].value) + ", "
                bfsList.pop(0)
        return order

    def tranverse(self):
        print("Tranverse tree using DFS (Depth-first search):")
        print("Pre-order  (Node -> Left -> Right): " + self.tranverseNLR(self.root)[0: -2])
        print("In-order   (Left -> Node -> Right): " + self.tranverseLNR(self.root)[0: -2])
        print("Post-order (Left -> Right -> Node): " + self.tranverseLRN(self.root)[0: -2] + "\n")
        print("Tranverse tree using BFS (Breadth-first search):")
        print("Level-order: " + self.tranverse_level_order(self.root)[0: -2])

if __name__ == "__main__":

#       Create Sample Tree
#            ___Z___
#           /       \
#       __A__      __B__
#      /     \    /     \
#     C       D  E       F

    binary_tree = BinaryTree("Z")
    binary_tree.root.left = Node("A")
    binary_tree.root.right = Node("B")
    binary_tree.root.left.left = Node("C")
    binary_tree.root.left.right = Node("D")
    binary_tree.root.right.left = Node("E")
    binary_tree.root.right.right = Node("F")
    
    binary_tree.tranverse()
