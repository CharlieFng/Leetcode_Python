class Solution(object):
    def checkSubarraySum(self, nums, k):

        dmap = {0 : -1}
        total = 0
        for i, n in enumerate(nums):
            total += n
            m = total % k if k else total
            if m not in dmap: dmap[m] = i
            elif dmap[m] + 1 < i: return True
        return False