# https: // leetcode.com/problems/binary-tree-maximum-path-sum/


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def maxPathSum(self, root):
        self.max_value = float("-inf")

        def traverse(root):
            if not root:
                return 0

            left = max(0, traverse(root.left))
            right = max(0, traverse(root.right))

            self.max_value = max(self.max_value, left + right + root.val)
            return max(left,right) + root.val
        
        traverse(root)
        return self.max_value




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
print(test.maxPathSum(a))
