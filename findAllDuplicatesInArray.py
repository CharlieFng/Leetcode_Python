class Solution(object):
    def findDuplicates(self, nums):
        
        ans = []
        for i in range(len(nums)):
            number = abs(nums[i])
            if nums[number-1] < 0 :
                ans.append(number)
                
            else:
                nums[number-1] *= -1 
        
        return ans
        """