class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if numRows == 1 or numRows >= len(s):
            return s

        idx = 0
        s_list = [''] * numRows
        going_down = False

        for char in s:
            s_list[idx] += char
            
            # 첫 번째 행이나 마지막 행에 도달하면 방향을 반전
            if idx == 0 or idx == numRows - 1:
                going_down = not going_down
            
            # 방향에 따라 현재 행을 증가 또는 감소
            if going_down:
                idx += 1
            else:
                idx -= 1

        return ''.join(s_list)

        