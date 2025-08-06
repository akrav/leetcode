class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_min = 1
        cur_max = 1

        total_max = -10000000
        for num in nums:
            if num == 0:
                cur_min = 1
                cur_max = 1
            
            new_val_one = cur_max * num
            new_val_two = cur_min * num
            cur_min = min(new_val_one, new_val_two, num)
            cur_max = max(new_val_one, new_val_two, num)

            total_max = max(total_max, cur_max)

        return total_max