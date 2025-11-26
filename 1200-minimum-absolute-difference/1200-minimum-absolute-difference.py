class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:

        arr.sort()
        n = len(arr)

        minimum_num = float(inf)

        for i in range(1, n):
            max_num = max(arr[i-1], arr[i])
            min_num = min(arr[i-1], arr[i])
            minimum_num = min(minimum_num, max_num-min_num)
        
        minimum_pair = []
        
        for i in range(1, n):
            max_num = max(arr[i-1], arr[i])
            min_num = min(arr[i-1], arr[i])
            
            if minimum_num == (max_num-min_num):
                minimum_pair.append([min_num,max_num])

        return minimum_pair
