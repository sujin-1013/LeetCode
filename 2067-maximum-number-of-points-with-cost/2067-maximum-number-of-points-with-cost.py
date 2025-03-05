class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        n = len(points)
        m = len(points[0])

        dp = [[0 for j in range(m)] for i in range(n)]
        dp[0] = points[0]


        for i in range(1,n):

            left = [0] * m
            left[0] = dp[i-1][0]
            for j in range(1, m):
                left[j] = max(left[j-1] - 1, dp[i-1][j])

            right = [0] * m
            right[m-1] = dp[i-1][m-1]
            for j in range(m-2,-1,-1):
                right[j] = max(right[j+1] - 1, dp[i-1][j])

            new_dp = [0] * m
            for j in range(m):
                new_dp[j] = points[i][j] + max(left[j], right[j])

            dp[i] = new_dp

        return max(dp[n-1])