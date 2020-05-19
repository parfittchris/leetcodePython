def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None

        while head and head.val == val:
            head = head.next

        curr = head
        prev = ListNode()
        prev.next = head

        while head:
            if head.val == val:
                prev.next = head.next
                head = head.next
            else:
                prev = prev.next
                head = head.next

        return curr


