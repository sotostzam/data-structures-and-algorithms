# Data Structures and Algorithms

## Data Structures

### Binary Tree

The binary tree is a tree data structure that contains nodes. Each node can hold a value and can have two children. A left node and a right node. Nodes without children are called leaves of the tree.

## Algorithms

### Depth-first Search (DFS)

Using *Depth-first search*, the search tree is deepened as much as possible on each child, and then moves on to the sibling nodes. There are three possible operations, tranverse the left node (L), tranverse the node itself (N) and tranverse the right node (R). With those in mind, there are also three different ways to tranverse a tree using DFS:

* **Pre-order (NLR)**
  * Access the value of the current node
  * Traverse the left child-node by recursively calling pre-order
  * Traverse the right child-node by recursively calling pre-order
* **In-order(LNR)**
  * Traverse the left child-node by recursively calling in-order
  * Access the data part of the current node
  * Traverse the right child-node by recursively calling in-order
* **Post-order (LRN)**
  * Traverse the left child-node by recursively calling post-order
  * Traverse the right child-node by recursively calling post-order
  * Access the data part of the current node

### Breadth-first Search (BFS)

Using *Breadth-first search*, the tree's root is explored first. From there the algorith then explores all of the neighbor nodes at the same depth (or layer), and then moves to a deeper layer, if it exists.
