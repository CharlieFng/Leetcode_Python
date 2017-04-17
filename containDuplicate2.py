class Solution(object):

	def containsNearbyDuplicate(self, nums, k):

		indexDic = dict()

		for i in range(len(nums)) :

			tmp = indexDic.get(nums[i])
			if tmp >= 0 and i-tmp <= k :
					return True
			else:
				indexDic[nums[i]] = i

		return False