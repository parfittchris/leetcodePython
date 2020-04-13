# https: // leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        temp_head = head
        final_head = ListNode(None)
        final_head.next = temp_head

        for i in range(n+1):
            if not head:
                return False
            else:
                head = head.next
        
        while head:
            head = head.next
            temp_head = temp_head.next
        
        temp_head.next = temp_head.next.next
        return final_head.next
        


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)

a.next = b
b.next = c
c.next = d
d.next = e

test = Solution()
print(test.removeNthFromEnd(a,2))
