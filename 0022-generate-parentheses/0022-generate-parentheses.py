class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def backtracking(ftn, left_cnt, right_cnt, n, li):
            
            if len(ftn) == (n*2):
                li.append(ftn)
                return

            if left_cnt < n:
                backtracking(ftn + "(", left_cnt+1, right_cnt, n, li)

            if right_cnt < left_cnt:
                backtracking(ftn + ")", left_cnt, right_cnt+1, n, li)

            print(ftn)

        answer = []
        backtracking("",0,0,n,answer)

        return answer