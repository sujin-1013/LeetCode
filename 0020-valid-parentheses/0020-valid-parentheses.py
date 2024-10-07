class Solution:
    def isValid(self, s: str) -> bool:


        stack_list = []
        mapping = {")":"(", "]":"[", "}":"{"}

        for char in s:
            if char in "([{":
                stack_list.append(char)
            else:
                if not stack_list or stack_list.pop() != mapping[char]:
                    return False

        return not stack_list
        