# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = head
        slow = head
        half = []

        while fast:
            fast = fast.next.next
            half.append(slow.val)
            slow = slow.next
        fast = 0
        for x in half[::-1]:
            x += slow.val
            slow = slow.next
            if x > fast:
                fast = x
        
        return fast