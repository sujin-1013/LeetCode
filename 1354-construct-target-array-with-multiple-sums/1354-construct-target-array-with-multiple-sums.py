import heapq

class Solution:
    def isPossible(self, target: List[int]) -> bool:


        if len(target) == 1:
            return target[0] == 1

        total_sum = sum(target)
        
        heap = []
        for i in range(len(target)):
            heapq.heappush(heap, -target[i])


        while heap:

            max_value = -heapq.heappop(heap)

            if max_value == 1:
                return True

            rest_sum = total_sum - max_value

            if rest_sum == 1:
                return True

            if rest_sum == 0 or max_value < rest_sum:
                return False

            pre_value = max_value % rest_sum

            heapq.heappush(heap, -pre_value)

            total_sum = rest_sum + pre_value

            print(heap)


        return False        