class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        pascal = [[1]]

        if numRows == 1:
            return pascal
        
        for i in range(1, numRows):
            row = [1]
            pre_row = pascal[i-1]

            for j in range(1,i):
                row.append(pre_row[j-1]+pre_row[j])
            
            row.append(1)

            pascal.append(row)
        
        return pascal