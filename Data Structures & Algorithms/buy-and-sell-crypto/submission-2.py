class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #use sliding window approach 
        #start with window size 1 itereate through size len(prices)
        if len(prices) < 2: # edge case of only one price
            return 0
        i = 0
        j = 1
        maxP = 0

        winSize = j - i

        while winSize < len(prices):
            #calculate the current sale
            sale = prices[j] - prices[i] 
            #check if it is greater than the current max
            maxP = max(maxP, sale)

            i += 1
            j += 1

            if j == len(prices):
                winSize += 1
                i = 0
                j = winSize
        
        return maxP
            
        