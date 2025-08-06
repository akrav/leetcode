class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        def is_possible(idx, fuel, used):
            if fuel < 0:
                return False
            if idx in used.keys() and used[idx]:
                return True

            old_fuel = fuel
            fuel = fuel + (gas[idx] - cost[idx])
            used[idx] = True
            old_idx = idx
            if idx ==len(gas) -1:
                idx = 0
            else:
                idx += 1
            print(f"start idx: {old_idx}, moving to idx: {idx}, old fuel: {old_fuel}, with this much fuel left at destination: {fuel}")

            ans = is_possible(idx, fuel, used)

            fuel = old_fuel
            used[idx] = False
            idx = old_idx

            return ans
            
        
        for i in range(len(gas)):
            print("\n\nnew round:")
            if is_possible(i, 0, {}):
                return i
        return -1