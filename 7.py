'''
https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
'''
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return None
        l, k = head, head.next.next
        while k and k.next:
            k,l = k.next.next,l.next
        l.next = l.next.next
        return head