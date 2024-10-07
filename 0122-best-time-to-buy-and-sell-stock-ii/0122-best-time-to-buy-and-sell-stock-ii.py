class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_price = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                total_price += (prices[i] - prices[i-1])

        return total_price