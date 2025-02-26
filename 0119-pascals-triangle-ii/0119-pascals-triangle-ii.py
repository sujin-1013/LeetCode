class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        pascal = {}
        pascal[0] = [1]

        if rowIndex == 0:
            return pascal[0]
        
        for i in range(rowIndex):
            pre_row = pascal[i]

            row = [1]

            for j in range(i):
                row.append(pre_row[j]+pre_row[j+1])

            row.append(1)

            pascal[i+1] = row
        
        return pascal[rowIndex]