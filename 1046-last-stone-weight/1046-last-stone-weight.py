import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        max_heap = []

        for stone in stones:
            heapq.heappush(max_heap, -stone)

        while True:
            if len(max_heap) >= 2:
                stone_1 = -heapq.heappop(max_heap)
                stone_2 = -heapq.heappop(max_heap)

                if stone_1 != stone_2:
                    heapq.heappush(max_heap, -(stone_1-stone_2))

            elif len(max_heap) == 1:
                return -heapq.heappop(max_heap)
            else:
                break

        return 0