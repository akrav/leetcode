class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def merge_sort(arr, l, r):
            
            if l >= r:
                return
            
            
            m = l + (r - l)//2
            merge_sort(arr, l, m)
            merge_sort(arr, m+1, r)

            arr_pointer = l
            list1 = arr[l:m+1]
            list2 = arr[m+1:r+1]
            l1_pointer = 0
            l2_pointer = 0

            while l1_pointer < len(list1) and l2_pointer < len(list2):

                if list1[l1_pointer] <= list2[l2_pointer]:
                    arr[arr_pointer] = list1[l1_pointer]
                    l1_pointer += 1
                else:
                    arr[arr_pointer] = list2[l2_pointer]
                    l2_pointer += 1
                arr_pointer += 1
            

            while l1_pointer < len(list1):
                arr[arr_pointer] = list1[l1_pointer]
                l1_pointer += 1
                arr_pointer += 1
            
            while l2_pointer < len(list2):
                arr[arr_pointer] = list2[l2_pointer]
                l2_pointer += 1
                arr_pointer += 1
            
            
            return
        
        merge_sort(nums, 0, len(nums)-1)


        