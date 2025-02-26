class Solution:
    def countBits(self, n: int) -> List[int]:
        answer = []
        for i in range(n+1):
            bin_str = ''
            n = i
            while True:
                bin_str += str(n % 2)
                n = n // 2
                if n <= 0:
                    break
            # print(bin_str)
            answer.append(sum(int(i) for i in list(bin_str)))

        return answer
            