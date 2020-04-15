# https: // leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def kthSmallest(self, root, k):
        queue = [root]
        nodes = []

        while len(queue):
            current = queue.pop(0)
            nodes.append(current.val)
            
            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)
        
        nodes = sorted(nodes)
        return nodes[k - 1]


a = TreeNode(3)
b = TreeNode(1)
c = TreeNode(4)
d = TreeNode(2)



a.left = b
a.right = c
c.right = d



test = Solution()
print(test.kthSmallest(a, 1))
