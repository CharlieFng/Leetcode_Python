class Solution(object):
    def maxProfit(self, prices):
        
        trans = 0
        if len(prices) <= 1:
            return trans
        else:
            low = prices[0]
            for i in range(1, len(prices)):
                if prices[i] > low:
                    trans = max(trans, (prices[i] - low))
                else:
                    low = prices[i]
        
        return trans