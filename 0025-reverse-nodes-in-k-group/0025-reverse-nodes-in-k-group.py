class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        dummy = ListNode(0)
        dummy.next = head
        g_prev = dummy

        while True:
            kth = g_prev
            for _ in range(k):
                kth = kth.next
                if kth is None:
                    return dummy.next

            g_next = kth.next
            prev = g_next
            curr = g_prev.next


            while curr and curr != g_next:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            
            temp = g_prev.next
            g_prev.next = kth
            g_prev = temp
            

        return dummy.next