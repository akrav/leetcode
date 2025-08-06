class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        left = 0
        right = len(people) -1
        boat = 0

        while left < right:
            total_weight = people[left] + people[right]

            if total_weight > limit:
                right -= 1  
            else:
                left += 1
                right -= 1
            
            boat += 1
        if left == right:
            boat += 1
        return boat