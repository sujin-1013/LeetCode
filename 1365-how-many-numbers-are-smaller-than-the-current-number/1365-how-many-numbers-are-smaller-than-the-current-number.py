class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_num = sorted(nums)
        answer = []
        for num in nums:
            answer.append(sorted_num.index(num))
        return answer
        