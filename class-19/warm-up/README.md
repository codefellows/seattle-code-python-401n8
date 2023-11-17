# Warm Up: Calculate Diameter of a Binary Tree

### Example 1: Simple Binary Tree

Consider the following binary tree:

```
    1
   / \
  2   3
 / \
4   5
```

In this tree, the longest path is from node 4 to node 3. The path is 4 -> 2 -> 1 -> 3. The length of this path, which is the diameter, is 3 (number of edges).

### Example 2: Unbalanced Tree

Now, consider an unbalanced tree:

```
    1
     \
      2
       \
        3
```

Here, the longest path is from node 1 to node 3, with the path being 1 -> 2 -> 3. The diameter is 2.

### Example 3: Complex Tree

Consider a more complex tree:

```
      1
     / \
    2   3
   / \
  4   5
     / \
    6   7
       /
      8
```

In this case, the longest path is from node 8 to node 3, going through nodes 7, 5, 2, and 1. The path is 8 -> 7 -> 5 -> 2 -> 1 -> 3, making the diameter 5.

### Calculating Diameter

The diameter can be calculated using various methods, one common approach being the use of depth-first search (DFS). The idea is to find the height of each left and right subtree for every node and add them to calculate the path through the node. The maximum of these sums at any node will give the diameter of the tree.

These examples illustrate how the diameter can vary depending on the structure of the tree, and it's not always about the height but rather the longest path between any two nodes.
