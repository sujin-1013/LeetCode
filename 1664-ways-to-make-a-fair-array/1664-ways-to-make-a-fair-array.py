class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        preEven = [0] * (n + 1)
        preOdd = [0] * (n + 1)

        # prefix sums 분리
        for i, x in enumerate(nums):
            preEven[i+1] = preEven[i]
            preOdd[i+1] = preOdd[i]
            if i % 2 == 0:
                preEven[i+1] += x
            else:
                preOdd[i+1] += x

        totalEven = preEven[n]
        totalOdd = preOdd[n]

        ans = 0
        for i in range(n):
            # 왼쪽 부분
            evenLeft = preEven[i]
            oddLeft = preOdd[i]

            # 오른쪽 부분 (짝/홀 뒤바뀜)
            evenRight = totalOdd - preOdd[i+1]
            oddRight = totalEven - preEven[i+1]

            if evenLeft + evenRight == oddLeft + oddRight:
                ans += 1

        return ans