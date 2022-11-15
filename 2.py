"""
https://leetcode.com/problems/remove-linked-list-elements/
203. Remove Linked List Elements
"""


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        cur = head
        if not head:
            return head
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        if head.val == val:
            head = head.next

        return head