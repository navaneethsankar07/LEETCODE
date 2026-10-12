class Solution:
    def mergeNodes(self, head: ListNode | None) -> ListNode | None:
        left = head
        right = head.next

        while right.next:
            if right.val == 0:
                left.next = right
                left = right
            else:
                left.val += right.val

            right = right.next

        left.next = None
        return head