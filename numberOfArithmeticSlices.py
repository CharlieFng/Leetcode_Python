class Solution(object):
    
    def numberOfArithmeticSlices(self, A):
        
        if len(A) < 3: return 0
        
        if len(A) == 3:
            if A[2] - A[1] == A[1] - A[0]:
                return 1
            else: return 0
        
        dif = A[1]-A[0]
        count = 1
        total = 0
        for i in range(2,len(A)):
            
            if A[i]-A[i-1] == dif:
                count += 1
            else:
                dif = A[i]-A[i-1]
                count = 1

            total = total + count-1
        return total