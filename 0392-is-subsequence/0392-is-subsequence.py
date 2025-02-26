class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        i = 0
        j = 0

        if s == "":
            return True

        if t == "":
            return False

        while True:
            if s[i] == t[j]:
                i += 1
            
            j += 1

            if i == len(s):
                return True
            
            if j == len(t):
                break

        return False