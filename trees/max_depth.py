# https: // leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        if not root:
            return -
        
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


        # def traverse(node):
        #     if not node.left and not node.right:
        #         return 0

        #     return max(traverse(node.left), traverse(node.right)) + 1
        
        # return traverse(root)

                

    
            


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
print(test.maxDepth(a))

#     3
#    / \
#   9  20
#     /  \
#    15   7
