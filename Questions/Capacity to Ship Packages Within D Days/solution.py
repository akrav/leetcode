class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        def canShip(capacity, days):
            count = 1
            total_weight = 0
            for item in weights:
                if total_weight + item <= capacity:
                    total_weight += item
                else:
                    total_weight = item
                    count += 1
            return count <= days


        while left < right:
            mid = left + (right - left)//2

            if canShip(mid, days):
                right = mid
            else:
                left = mid + 1
            
        return left