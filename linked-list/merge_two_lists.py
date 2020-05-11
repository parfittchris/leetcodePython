# https: // leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        temp = ListNode(None)
        new_head = temp

        while l1 or l2:
            left = None
            right = None


            if l1:
                left = l1.val
            else:
                left = float("inf")
            
            if l2:
                right = l2.val
            else:
                right = float("inf")
            
            if left > right:
                temp.next = ListNode(right)
                l2 = l2.next
                temp = temp.next
            else:
                temp.next = ListNode(left)
                l1 = l1.next
                temp = temp.next

        
        return new_head.next

      
            


a = ListNode(1)
b = ListNode(2)
c = ListNode(4)
d = ListNode(1)
e = ListNode(3)


a.next = b
b.next = c

d.next = e

test = Solution()
print(test.mergeTwoLists(a, d))
