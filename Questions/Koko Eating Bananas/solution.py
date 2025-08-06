class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def eating_time(eating_rate):
            total_time = 0
            for pile in piles:
                total_time += math.ceil(pile/eating_rate)
            return total_time
        
        low = 1
        high = max(piles)

        while low < high:
            eating_rate = low + (high - low)//2

            hours_taken = eating_time(eating_rate)

            # if taking too long, increase lower bound of eating rate
            if hours_taken > h:
                low = eating_rate + 1
            else:
                high = eating_rate
        
        return low
            
        