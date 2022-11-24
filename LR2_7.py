'''
[268. Missing Number](https://leetcode.com/problems/missing-number/)
'''
class Solution:
	def missingNumber(self, nums: List[int]) -> int:
		n = len(nums)
		total_sum = (n*(n+1)) // 2

		arr_sum = 0
		for item in nums:
			arr_sum += item
		return total_sum-arr_sum