class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:

        answer = []
        i = 0
        idx = 0

        while True:
            if idx >= len(target):
                return answer
                break
            if target[idx] == (i+1):
                answer.append("Push")
                i += 1
                idx += 1
            else:
                answer.append("Push")
                answer.append("Pop")
                i += 1
            # print(i, answer)
        