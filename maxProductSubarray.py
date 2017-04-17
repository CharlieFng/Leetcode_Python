class Solution(object):

	def maxProduct(self, nums):
		if len(nums) == 0:
			return 0

		res = curMax = curMin = nums[0]
		for i in range(1, len(nums)):
			
			tmp = curMax
			curMax = max(curMax*nums[i],curMin*nums[i],nums[i])
			curMin = min(curMin*nums[i],tmp*nums[i],nums[i]) 

			res = max(res,curMax)

		return res
