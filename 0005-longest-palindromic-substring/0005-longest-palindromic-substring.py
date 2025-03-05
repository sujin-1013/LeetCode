class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        answer = ""

        for i in range(n):
            for j in range(n-1,i-1,-1):
                # print(i,j)
                new_s = s[i:j+1]
                # print(new_s)
                # print(new_s[::-1])
                if new_s == new_s[::-1]:
                    if len(new_s) > len(answer):
                        answer = new_s

        return answer
        