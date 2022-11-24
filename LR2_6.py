'''
[912. Sort an Array](https://leetcode.com/problems/sort-an-array/)
'''
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        else:
            treshold_ind = len(nums) // 2
            treshold = nums.pop(treshold_ind)
            less = [x for x in nums if x <= treshold]
            greater = [x for x in nums if x > treshold]
            return self.sortArray(less) + [treshold] + self.sortArray(greater)