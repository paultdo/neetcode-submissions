class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        l, r = 0, 0

        while r < len(prices):
            profit = prices[r] - prices[l]

            maximum = max(profit, maximum)

            if prices[l] < prices[r]:
                r += 1
            elif prices[l] > prices[r]:
                l += 1
            else:
                r += 1
        
        return maximum


            