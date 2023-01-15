# Maximum Depth of Binary Tree
# Given the root of a binary tree return its maximum depth
# Technique used: Depth First Search
from class_node import Node
from collections import deque 


# Recursive DFS
def maxDepth_dr(root: Node) -> int:
    # if the root is null return zero
    if not root:
        return 0

    return 1 + max(maxDepth_dr(root.left), maxDepth_dr(root.right))

# Iterative BFS - count the number of levels which will be the max depth - involves queue
def maxDepth_b(root: Node) -> int:
    # if the root is null return zero
    if not root:
        return 0

    level = 1
    q = deque([root])

    while q:
        for i in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)    

        level += 1


# Iterative DFS solution -  we will be using stack
def maxDepth_di(root: Node):
    if not root:
        return 0

    stack = [[root,1]]
    result = 1

    while stack:
        node, depth = stack.pop()

        if node:
            result = max(result, depth)
            stack.extend([node.left, depth+1])
            stack.extend([node.right, depth+1])

    return result


