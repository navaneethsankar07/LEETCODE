# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        index = 0
        current = list1
        start = None
        end = None
        while current:
            if index == a-1:
                start = current
            if index == b:
                end = current.next
                break
            current = current.next
            index += 1
            
        start.next = list2

        while list2.next:
            list2 = list2.next
        
        list2.next = end
    
        return list1