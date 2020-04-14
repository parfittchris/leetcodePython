# https: // leetcode.com/problems/same-tree/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSameTree(self, p, q):
        same_tree = True

        def traverse(left, right):
            if not left and not right:
                return True

            if not left or not right or left.val != right.val:
                return False
            
            return traverse(left.left, right.left) and traverse(left.right, right.right)

        return traverse(p, q)


a = TreeNode(2)
b = TreeNode(9)
c = TreeNode(20)

d = TreeNode(2)
e = TreeNode(9)
f = TreeNode(20)

a.left = b
a.right = c

d.left = e
d.right = f

test = Solution()
print(test.isSameTree(a, d))
