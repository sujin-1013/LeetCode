class Solution:
    def romanToInt(self, s: str) -> int:
        
        dic_symbol = {"I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
        }
        number = 0
        check = 0
        for i in range(len(s)-1):
            now_s = s[i]
            next_s = s[i+1]
            if dic_symbol[now_s] < dic_symbol[next_s]:
                check = 1
                not_sum = dic_symbol[next_s] - dic_symbol[now_s]
            else:
                if check == 1:
                    number += not_sum
                    check = 0
                else:
                    number += dic_symbol[now_s]
            print(now_s, number)
        if check == 1:
            number += not_sum
        else:
            number += dic_symbol[s[-1]]

        return number