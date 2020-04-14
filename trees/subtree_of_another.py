# https: // leetcode.com/problems/subtree-of-another-tree/


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        queue = [s]

        while len(queue):
            current = queue.pop(0)

            if current.val == t.val:
                if self.isSameTree(current, t) == True:
                    return True
            
            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)
        
        return False



    def isSameTree(self, p, q):

        def traverse(left, right):
            if not left and not right:
                return True

            if not left or not right or left.val != right.val:
                return False

            return traverse(left.left, right.left) and traverse(left.right, right.right)

        return traverse(p, q)


a = TreeNode(3)
b = TreeNode(4)
c = TreeNode(5)
d = TreeNode(1)
e = TreeNode(2)

f = TreeNode(4)
g = TreeNode(1)
h = TreeNode(2)

a.left = b
a.right = c
b.left = d
b.right = e

f.left = g
f.right = h


test = Solution()
print(test.isSubtree(a, f))

