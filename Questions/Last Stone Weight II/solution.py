class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stone_sum = sum(stones)
        target = (stone_sum + 1)//2
        memo = {}


        #the goal is to get 0, so if the sum is 38 we are looking for stones adding to 19
        # if the sum is 39 we will have at best value of 1 left since 19 will cancel with 19 stones leaving 1
        # so we really have a target of 19 that if we reach -1 we found out answer
    
        def rec(i, val):
            print(f"val <= 0: {val <= 0}, i == len(stones): {i == len(stones)}")
            if val <= 0 or i == len(stones):
                pile1 = stone_sum - target - abs(val)
                pile2 = target + abs(val)
                print(f"stone_sum: {stone_sum}, target: {target}, val: {val}, pile1: {pile1}, pile2: {pile2}")

                return pile2 - pile1
            if (i, val) in memo:
                return memo[(i,val)]
            
            memo[(i,val)] = min(rec(i + 1, val), rec(i + 1, val - stones[i]))
            return memo[(i,val)]
        
        return rec(0, target)