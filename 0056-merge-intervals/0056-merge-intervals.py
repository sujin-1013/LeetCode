class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # 1. 시작 시간을 기준으로 오름차순 정렬
        intervals.sort(key=lambda x: x[0])

        # 2. 결과 리스트에 첫 번째 구간을 미리 넣어두고 시작
        merged = [intervals[0]]

        # 3. 두 번째 구간부터 끝까지 순회
        for current in intervals[1:]:
            # 결과 리스트의 가장 마지막 구간(방금 넣은 것)을 가져옴
            last_merged = merged[-1]

            # 4. 겹치는지 확인: (앞 구간의 끝 >= 뒷 구간의 시작)
            if last_merged[1] >= current[0]:
                # 겹친다면? -> 구간 합치기 (끝나는 시간을 둘 중 더 큰 값으로 연장)
                last_merged[1] = max(last_merged[1], current[1])
            else:
                # 안 겹친다면? -> 현재 구간을 그대로 결과 리스트에 추가
                merged.append(current)

        return merged