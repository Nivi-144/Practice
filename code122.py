class Solution:
    def maxProfit(self, prices):
        maximum_profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                maximum_profit += prices[i] - prices[i - 1]

        return maximum_profit
