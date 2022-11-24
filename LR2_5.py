'''
- [1539. Kth Missing Positive Number](https://leetcode.com/problems/kth-missing-positive-number/)
'''
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        ss, x = set(arr), 1
        while True:
            if x not in ss: k -= 1
            if not k: return x
            x += 1