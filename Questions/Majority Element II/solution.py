class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        target = n // 3

        count_dic = defaultdict(int)
        nums_pointer = 0

        for i in range(len(nums)):
            num = nums[i]
            count_dic[num] += 1

            if count_dic[num] == target+1:
                nums[nums_pointer] = num
                nums_pointer += 1
        return nums[:nums_pointer]
        