class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        times = [0] * n

        pre_time = 0

        for log in logs:
            l = log.split(":")
            state = l[1]
            idx = int(l[0])
            cur_time = int(l[-1]) 

            # start
            if "start" == state:
                if stack:
                    pre_idx, _ = stack[-1]
                    times[pre_idx] += cur_time - pre_time
 
                stack.append((idx, cur_time))
                pre_time = cur_time

            # end
            else:
                poped_idx, start_time = stack.pop()
                total_time = cur_time - pre_time + 1
                times[poped_idx] += total_time

                pre_time = cur_time + 1

        return times
        