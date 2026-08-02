# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head and not head.next:
            return head
        
        fast = head.next
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        last = slow
        slow = slow.next
        last.next = None
        
        prev = None

        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        
        max_twin_sum = 0

        while head and prev:
            max_twin_sum = max(max_twin_sum, head.val + prev.val)
            head = head.next
            prev = prev.next
        

        return max_twin_sum
