class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []

        def rec(start, combination_arr):
            if len(combination_arr) == k:
                results.append(combination_arr[:])
                return
            
            for i in range(start, n+1):
                # if i > start and 
                combination_arr.append(i)
                rec(i + 1, combination_arr)
                combination_arr.pop()
            
            return

        
        rec(1, [])

        return results