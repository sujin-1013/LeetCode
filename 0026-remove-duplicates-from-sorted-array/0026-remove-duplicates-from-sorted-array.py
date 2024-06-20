class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        new_list = []

        for num in nums:
            if num not in new_list:
                new_list.append(num)
        
        k = len(new_list)

        for i in range(k):
            nums[i] = new_list[i]


        return k