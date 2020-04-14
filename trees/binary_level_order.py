# https: // leetcode.com/problems/binary-tree-level-order-traversal/


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        if not root:
            return None

        level_total = 1 
        next_level = 0

        queue = [root]
        current_level = []
        results = []

        while len(queue):
            current = queue.pop(0)
            level_total -= 1
            current_level.append(current.val)

            if current.left:
                next_level += 1
                queue.append(current.left)

            if current.right:
                next_level += 1
                queue.append(current.right)

            if level_total == 0:
                level_total = next_level
                next_level = 0
                results.append(current_level)
                current_level = []

        return results
            


a = TreeNode(3)
b = TreeNode(9)
c = TreeNode(20)
d = TreeNode(15)
e = TreeNode(7)


a.left = b
a.right = c
c.left = d
c.right = e

test = Solution()
print(test.levelOrder(a))

# [
#     [3],
#     [9, 20],
#     [15, 7]
# ]
