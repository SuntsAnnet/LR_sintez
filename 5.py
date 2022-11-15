'''
https://leetcode.com/problems/merge-nodes-in-between-zeros/
'''
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr = head
        while(curr):
                s, t, curr = 0, curr, curr.next
                while curr.val != 0:
                    s += curr.val
                    curr = curr.next
                t.val = s
                if curr.next:
                    t.next = curr
                else:
                    t.next = None
                    break
        return head