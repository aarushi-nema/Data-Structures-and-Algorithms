# leetcode link: https://leetcode.com/problems/binary-tree-inorder-traversal/
# left - root - right
# O(n); n->no of nodes

from class_node import Node

#recursive solution
def inorderTraversal_recursive(root: Node):
    result = []

    # nested function
    def inorder(root):
        if not root:
            return
        inorder(root.left)
        result.append(root.val)
        inorder(root.right)

    inorder(root)
    return result