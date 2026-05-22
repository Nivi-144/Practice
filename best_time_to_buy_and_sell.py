class Solution:
    def maxProfit(self, prices):
        minimum_price = float('inf')
        maximum_profit = 0

        for price in prices:
            if price < minimum_price:
                minimum_price = price
            elif price - minimum_price > maximum_profit:
                maximum_profit = price - minimum_price

        return maximum_profit
