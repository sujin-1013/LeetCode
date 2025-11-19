class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        heights = [0] + heights + [0]
        stack = []
        max_area = 0
        n = len(heights)

        for i in range(n):
            
            while stack:
                if heights[stack[-1]] > heights[i]:
                    pre_idx = stack.pop()
                    h = heights[pre_idx]
                    right_idx = i
                    left_idx = stack[-1]
                    w = right_idx - left_idx - 1

                    area = w * h

                    max_area = max(max_area, area)
                else:
                    break

            stack.append(i)

        return max_area