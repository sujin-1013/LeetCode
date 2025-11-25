class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        two_sum = {}

        for i, num in enumerate(nums):
            if target - num in two_sum:
                return [two_sum[target-num], i]
            two_sum[num] = i

        
        