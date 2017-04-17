class Solution(object):
    def findMaxLength(self, nums):
        
        
        if nums == []: return 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1
                
        
        sums = [0] * len(nums)
        res = 0
        dic = dict()
        dic[0] = -1
        
        for i in range(len(nums)):
            if i == 0 : sums[i] = nums[i]
            else: sums[i] = sums[i-1] + nums[i]
            
            if sums[i] in dic:
                tmp = dic[sums[i]]
                res = max(res, i-tmp)
            else:
                dic[sums[i]] = i
                
        return res