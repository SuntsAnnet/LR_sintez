'''
- [977. Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/)

'''
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        l ,r = 0,len(A)-1
        res = []
        while l <= r:
            if A[r]**2 >= A[l]**2:
                res.append(A[r]**2)
                r -= 1
            else:
                res.append(A[l]**2)
                l += 1
        return res[::-1]