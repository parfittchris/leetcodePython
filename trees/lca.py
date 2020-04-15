# https: // leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
      if not root:
          return
      elif p < root.val and q < root.val:
          return self.lowestCommonAncestor(root.left, p, q)
      elif p > root.val and q > root.val:
          return self.lowestCommonAncestor(root.right, p, q)
      else:
          return root.val  


a = TreeNode(6)
b = TreeNode(2)
c = TreeNode(8)
d = TreeNode(0)
e = TreeNode(4)
f = TreeNode(7)
g = TreeNode(9)
h = TreeNode(3)
j = TreeNode(5)


a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g
e.left = h
e.right = j


test = Solution()
print(test.lowestCommonAncestor(a, 2, 8))
