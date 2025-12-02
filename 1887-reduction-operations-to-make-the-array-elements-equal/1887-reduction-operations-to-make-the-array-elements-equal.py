class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        
        nums.sort()

        total = 0
        operation = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                operation += 1
            total += operation

        return total