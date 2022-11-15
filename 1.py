 """
 https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/description/
 Convert Binary Number in a Linked List to Integer
 """
 #Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        l = []
        while head is not None:
            l.append(head.val)
            head=head.next
        k=l[::-1]
        l=0
        for i,t in enumerate(k):
            l+= t*2**i
        return (l)