class Solution(object):
    def divide(self, dividend, divisor):
        
        if divisor == 0 :
            return 2147483647
        if dividend == 0 :
            return 0
        
        a = abs(dividend)
        b = abs(divisor)
        
        res = 0
        while a >= b:
            count = 1
            sum = b
            while sum + sum <= a:
                sum += sum
                count += count
            a -= sum
            res += count

        
        
        
        
        return res if (dividend> 0 and divisor > 0) or  (dividend<0 and divisor<0) else -res