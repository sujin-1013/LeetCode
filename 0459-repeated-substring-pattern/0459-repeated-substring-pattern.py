class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:

        new_s = s * 2

        if s in new_s[1:len(new_s)-1]:
            return True
            
        return False 
        