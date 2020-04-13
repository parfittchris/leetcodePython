# https: // leetcode.com/problems/reverse-linked-list/

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def reverseList(self, head):
        pre = None

        while head:
            next = head.next
            head.next = pre
            pre = head
            head = next
        
        return pre

        




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
print(test.reverseList(a))