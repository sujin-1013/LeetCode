class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        n = len(temperatures)
        wait = [0] * n

        for i in range(n):
            while stack:
                if temperatures[stack[-1]] < temperatures[i]:
                    pre_idx = stack.pop()
                    wait[pre_idx] = i - pre_idx
                else:
                    break

            stack.append(i)
            # print(i, stack, wait)
        
        return wait