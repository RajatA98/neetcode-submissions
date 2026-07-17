class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        sale = 0
        i = 0
        ws = 1
        j = i + ws
        while ws < (len(prices)): 
            sale = prices[j] - prices[i]
            if sale > max_profit:
                max_profit = sale
            i += 1
            j = i + ws
            if j >= len(prices):
                ws += 1
                i = 0
                j = i + ws

        return max_profit