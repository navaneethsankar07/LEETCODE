# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: ListNode | None) -> ListNode | None:
        self.left = head
        self.right = head.next
        
        while self.right.next:
            if self.right.val != 0:
                self.left.val += self.right.val
                self.left.next = self.right.next
            else:
                self.left = self.right
            
            self.right = self.right.next
        
        self.left.next = None

        return head