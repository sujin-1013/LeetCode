class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # n = len(prices)

        # max_profit = 0

        # for i in range(n):
        #     for j in range(i+1,n):
        #         if (prices[j] - prices[i]) > max_profit:
        #             max_profit = prices[j] - prices[i]

        # return max_profit
        
        n = len(prices)

        profit = 0
        
        buy = prices[0]

        for i in range(1,n):
                if prices[i] < buy:
                    buy = prices[i]
                elif prices[i] - buy > profit:
                    profit = prices[i] - buy

        return profit