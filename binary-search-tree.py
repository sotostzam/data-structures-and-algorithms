import os
import random
binary_tree = __import__("binary-tree")

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Function to add a value into the node recursively
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

class BinarySearchTree(binary_tree.BinaryTree):
    def __init__(self):
        self.root = None

    # Wrapper function to add a value into the BST
    def insert(self, value: int):
        if self.root == None:
            self.root = Node(value)
        else:
            self.root.insert(value)

    # Function to search for a value into the BST
    def search(self, value):
        current_node = self.root
        step = 0
        while True:
            print(str(step) + ". Check Node with value " + str(current_node.value))
            if current_node != None and current_node.value != value:
                if value < current_node.value:
                    print("   ↳ Target value is less than node's value (" + str(value) + " < " + str(current_node.value) + ")")
                    if current_node.left != None:
                        print("   ↳ Move and search the left node")
                        current_node = current_node.left
                    else:
                        print("   ↳ Node does not have a left child.")
                        print("   ↳ Value does not exist")
                        break
                elif value > current_node.value:
                    print("   ↳ Target value is greater than node's value (" + str(value) + " > " + str(current_node.value) + ")")
                    if current_node.right != None:
                        print("   ↳ Move and search the right node")
                        current_node = current_node.right
                    else:
                        print("   ↳ Node does not have a left child.")
                        print("   ↳ Value does not exist")
                        break
            else:
                print("   ↳ Target value found!")
                break
            step += 1

if __name__ == "__main__":
    def showMenu():
        while True:
            try:
                print("Please enter your choice:\n" +
                    "1. Search value\n" +
                    "0. Quit\n")
                selection = int(input("Your selection: "))
                print()
                if selection == 0:
                    quit()
                elif selection == 1:
                    selection = int(input("Value to search for: "))
                    tree.search(selection)
                    print()
                else: 
                    raise ValueError
            except ValueError:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Wrong input.\n")
                pass

    tree = BinarySearchTree()

    tempString = 'Random numbers inserted into tree: \n'
    for i in range(0, 10):
        num = random.randint(0, 100)
        tree.insert(num)
        if i != 9:
            tempString += str(num) + ', '
        else:
            tempString += str(num)
    print(tempString + "\n")

    tree.tranverse()
    print("Height of root Node: " + str(tree.find_height(tree.root)))
    print("Depth of the tree  : " + str(tree.depth(tree.root)))
    print("Size of the tree   : " + str(tree.size()) + "\n")

    showMenu()
