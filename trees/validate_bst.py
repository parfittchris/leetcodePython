# https: // leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root, high= float("inf"), low= float("-inf")):
        if not root:
            return True
        elif root.val >= high or root.val <= low:
            return False
        else:
            return self.isValidBST(root.left, min(high, root.val), low) and self.isValidBST(root.right, high, max(low, root.val))
            



a = TreeNode(5)
b = TreeNode(1)
c = TreeNode(10)
d = TreeNode(8)
e = TreeNode(11)


a.left = b
a.right = c
c.left = d
c.right = e



test = Solution()
print(test.isValidBST(a))

#     5
#    / \
#   1   4
#      / \
#     3   6
