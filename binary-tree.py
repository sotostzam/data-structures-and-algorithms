import random 

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

    def tranverseNLR(self, order = ''):
        order += str(self.value) + ", "
        if self.left != None:
            order += self.left.tranverseNLR()   
        if self.right != None:
            order += self.right.tranverseNLR()
        return order

    def tranverseLNR(self, order = ''):
        if self.left == None:
            order += str(self.value) + ", "
        else:
            order += self.left.tranverseLNR()
            order += str(self.value) + ", "
        if self.right != None:
            order += self.right.tranverseLNR()
        return order

    def tranverseLRN(self, order = ''):
        if self.left != None:
            order += self.left.tranverseLRN()
        if self.right != None:
            order += self.right.tranverseLRN()
        order += str(self.value) + ", "
        return order

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value: int):
        if self.root == None:
            self.root = Node(value)
        else:
            self.root.insert(value)

    def tranverse(self):
        print("Tranverse tree using DFS (Depth-first search):")
        print("Pre-order  (NLR): " + self.root.tranverseNLR()[0: -2])
        print("In-order   (LNR): " + self.root.tranverseLNR()[0: -2])
        print("Post-order (LRN): " + self.root.tranverseLRN()[0: -2])

    def structure(self, bfsList = [], layer = 0):
        if layer == 0:
            if self.root == None:
                print("Tree is empty.")
                return 0
            else:
                bfsList.append(self.root)

        nodeList = len(bfsList)
        tempString = ''

        # Check if none only
        flag = True
        for i in range(0, nodeList):
            if bfsList[i] != None:
                flag = False
        if flag == False :
            for i in range(0, nodeList):
                if bfsList[0] == None:
                    if i == nodeList-1:
                        tempString += "-"
                    else:
                        tempString += "-, "
                    bfsList.append(None)
                    bfsList.append(None)
                elif bfsList[0].left != None or bfsList[0].right != None:
                    if bfsList[0].left != None:
                        bfsList.append(bfsList[0].left)
                    else:
                        bfsList.append(None)
                    if bfsList[0].right != None:
                        bfsList.append(bfsList[0].right)
                    else:
                        bfsList.append(None)
                    if i == nodeList-1:
                        tempString += str(bfsList[0].value)
                    else:
                        tempString += str(bfsList[0].value) + ", "
                else:
                    if i == nodeList-1:
                        tempString += str(bfsList[0].value)
                        bfsList.append(None)
                        bfsList.append(None)
                    else:
                        tempString += str(bfsList[0].value) + ", "
                        bfsList.append(None)
                        bfsList.append(None)
                bfsList.pop(0)

            if layer == 0:
                print("Root   : " + tempString)
            else:
                print("Layer " + str(layer) + ": " + tempString)    
            layer += 1
            if len(bfsList) != 0:
                self.structure(bfsList, layer)

# Initialization of the Binary Tree
binary_tree = BinaryTree()

# Test random values
tempString = 'Random numbers inserted into tree: \n'
for i in range(0, 10):
    num = random.randint(0, 100)
    binary_tree.insert(num)
    if i != 9:
        tempString += str(num) + ', '
    else:
        tempString += str(num)
print(tempString + "\n")

binary_tree.tranverse()

print("\nTree structure using BFS (Breadth-first search):")
binary_tree.structure()