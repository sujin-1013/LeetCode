class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        new_list = []

        for i in range(m):
            new_list.append(nums1[i])

        for i in range(n):
            new_list.append(nums2[i])
        new_list.sort()

        for i in range(len(new_list)):
            nums1[i] = new_list[i]
        return nums1

