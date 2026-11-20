class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode(0, head)
        curr = dummy
        prev = dummy
        for _ in range(n + 1):
            curr = curr.next
        
        while curr:
            curr = curr.next
            prev = prev.next
        
        prev.next = prev.next.next

        return dummy.next