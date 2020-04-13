# https: // leetcode.com/problems/linked-list-cycle/

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        seen = {}

        while head.next:
            if head.val in seen:
                return True

            seen[head.val] = True
            head = head.next
        
        return False

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = c

test = Solution()
print(test.hasCycle(a))
