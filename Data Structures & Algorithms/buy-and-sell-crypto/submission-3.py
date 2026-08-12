class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #buy low sell high
        #traverse through the prices array
        #keep track of the min price
        #calculate 
        minP =  prices[0]

        maxP = 0

        for p in prices:
            #get current sale 
            profit = p - minP

            #update min p
            minP = min(minP,p)
            #update max profit
            maxP = max(maxP, profit)

        return maxP
