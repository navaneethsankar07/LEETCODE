import math
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current.next:
            gcd = math.gcd(current.val,current.next.val)
            new_node = ListNode(gcd)
            new_node.next = current.next
            current.next = new_node
            current = current.next.next
        return head
