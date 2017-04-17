class Solution(object):
    
    def twoSum(self, numbers, target):
        
        length = len(numbers)
        for i in range(0,length-1):
            result = self.binarySearch(i,length,numbers,target-numbers[i])
            if(result!=-1):
                return (i+1,result+1)

                
    def binarySearch(self,start,end,numbers,num):
        middle = start + (end - start)/2
        if  start<middle<end:
            if numbers[middle] == num:
                return middle
            elif numbers[middle] > num:
                return self.binarySearch(start,middle,numbers,num)
            else:
                return self.binarySearch(middle,end,numbers,num)
        else:
            return -1