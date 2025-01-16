class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # 두 문자열 길이를 맞추기 위해 0으로 패딩
        num1 = num1.zfill(max(len(num1), len(num2)))
        num2 = num2.zfill(max(len(num1), len(num2)))
        
        save = 0  # 캐리 저장
        answer = []  # 결과 저장
        
        # 뒤에서부터 순회
        for i in range(len(num1) - 1, -1, -1):
            n1, n2 = int(num1[i]), int(num2[i])
            n = n1 + n2 + save  # 두 자리 숫자와 캐리 더하기
            
            answer.append(str(n % 10))  # 현재 자리 숫자 추가
            save = n // 10  # 캐리 업데이트
        
        # 마지막 캐리가 남아 있으면 추가
        if save:
            answer.append(str(save))
        
        # 결과를 뒤집어서 반환
        return ''.join(answer[::-1])