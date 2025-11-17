class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        correct_li = [i for i in range(1,n+1)]
        lost_num = set(correct_li)-set(nums)

        check_li =[]

        for num in nums:
            if num not in check_li:
                check_li.append(num)
            else:
                repeated_num = num
                break
        return [repeated_num, list(lost_num)[0]]
            
            
        