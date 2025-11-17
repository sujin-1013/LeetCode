class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        max_cnt = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 1:
                cnt += 1
                max_cnt = max(max_cnt, cnt)
            else:
                cnt = 0
                max_cnt = max(max_cnt, cnt)
        return max_cnt
        