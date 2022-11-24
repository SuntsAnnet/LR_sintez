'''
- [852. Peak Index in a Mountain Array](https://leetcode.com/problems/peak-index-in-a-mountain-array/)

'''
class Solution:
    def peakIndexInMountainArray(self, arr):
        l, r = 1, len(arr)-2

        while l <= r: # O(log(n))
            m = (l+r)//2
            mid = arr[m]
            leftfMid = arr[m-1]
            rightfMid = arr[m+1]

            if  mid > leftfMid and mid > rightfMid:
                return m
            elif mid < leftfMid:
                r = m-1
            else:
                l = m+1