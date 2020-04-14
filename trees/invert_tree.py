# https: // leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        if not root:
            return None

        
        def traverse(node):
            temp = node.left
            node.left = node.right
            node.right = temp

            if node.left: 
                traverse(node.left)
            if node.right:
                traverse(node.right)


        traverse(root)
        return root



a = TreeNode(4)
b = TreeNode(7)
c = TreeNode(2)
d = TreeNode(9)
e = TreeNode(6)
f = TreeNode(3)
g = TreeNode(1)


a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g

test = Solution()
print(test.invertTree(a))

