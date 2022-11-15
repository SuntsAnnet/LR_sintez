"""""
https://leetcode.com/problems/odd-even-linked-list/
"""""
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        odd = head.next
        curr = head
        while curr.next:
            curr.next,curr  = curr.next.next,curr.next
        curr = head
        while curr.next:
            curr = curr.next
        curr.next = odd
        return head