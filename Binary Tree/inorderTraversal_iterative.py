# leetcode link: https://leetcode.com/problems/binary-tree-inorder-traversal/
# left - root - right
# O(n); n->no of nodes

from class_node import Node

#recursive solution
def inorderTraversal_recursive(root: Node):
    result = []
    stack = []
    current = root

    while current or stack:
        while current:
            stack.append(current)
            current.left
        current = stack.pop()
        result.append(current)
        current = current.right

    return result