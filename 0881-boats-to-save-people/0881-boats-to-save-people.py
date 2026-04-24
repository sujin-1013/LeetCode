class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        n = len(people)

        people.sort()

        left = 0
        right = n-1

        cnt = 0

        while left <= right:
            cnt += 1
            if people[left] + people[right] <= limit:

                left += 1 
                right -= 1
            else:
                right -= 1

        return cnt