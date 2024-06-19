class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        new_nums = []
        
        for num in nums:
            if num != val:
                new_nums.append(num)

        k = len(new_nums)

        for i in range(k):
            nums[i] = new_nums[i]

        return k