class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        correct = set(range(1,max(max(nums),len(nums))+1))

        return list(correct-set(nums))