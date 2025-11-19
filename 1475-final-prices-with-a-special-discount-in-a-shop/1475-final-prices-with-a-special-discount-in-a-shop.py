class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:

        n = len(prices)
        discounts = [0] * n

        for i in range(n):
            j = i + 1
            while True:
                if j >= n or i+1 == n or prices[i] < min(prices[i+1:]):
                    discounts[i] = prices[i]
                    break 
                if prices[j] <= prices[i]:
                    discounts[i] = prices[i] - prices[j]
                    break
                else: 
                    j += 1
                
        return discounts