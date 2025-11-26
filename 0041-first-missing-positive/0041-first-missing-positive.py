class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        n = len(nums)

        if 1 not in nums:
            return 1
        
        if n == 1:
            return 2

        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1

        print(nums)

        for i in range(n):
            idx = abs(nums[i])

            if 1 <= idx <= n:
                if nums[idx-1] > 0:
                    nums[idx-1] = -nums[idx-1]

        print(nums)

        for i in range(n):
            if nums[i] > 0:
                return i+1

        return n+1
