class Solution:
    def romanToInt(self, s: str) -> int:
        dic_symbol = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        number = 0
        
        for i in range(len(s) - 1):
            # 다음 값이 더 크면 뺄셈, 아니면 덧셈
            if dic_symbol[s[i]] < dic_symbol[s[i + 1]]:
                number -= dic_symbol[s[i]]
            else:
                number += dic_symbol[s[i]]
        
        # 마지막 문자는 항상 더함
        number += dic_symbol[s[-1]]
        
        return number
