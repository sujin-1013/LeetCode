class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        if len(s) != len(goal):
            return False

        new_s = s * 2

        if goal in new_s:
            return True
        
        return False
        