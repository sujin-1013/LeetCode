class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for num in nums:
            if num not in dic.keys():
                dic[num] = 1
            else:
                dic[num] += 1
        
        for num, cnt in dic.items():
            if cnt > len(nums) // 2:
                return num