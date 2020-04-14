# https: // leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        if inorder:
            idx = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[idx])
            root.left = self.buildTree(preorder, inorder[0:idx])
            root.right = self.buildTree(preorder, inorder[idx + 1:])
            return root





preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

test = Solution()
print(test.buildTree(preorder, inorder))
