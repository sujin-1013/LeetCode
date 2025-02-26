class Solution:
    def climbStairs(self, n: int) -> int:
        climb_dict = {}

        if n == 1:
            return 1

        def dp(k):

            if k == 1:
                return 1
            if k == 2:
                return 2

            if k in climb_dict:
                return climb_dict[k]

            climb_dict[k] = dp(k-1) + dp(k-2)

            return climb_dict[k]

        return dp(n)