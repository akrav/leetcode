class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        ans_pointer = m + n - 1
        nums1_pointer = m - 1
        nums2_pointer = n - 1

        while nums1_pointer >= 0 and nums2_pointer >= 0:

            n1_val = nums1[nums1_pointer]
            n2_val = nums2[nums2_pointer]

            if n2_val > n1_val:
                nums1[ans_pointer] = n2_val
                nums2_pointer -= 1
            else:
                nums1[ans_pointer] = n1_val
                nums1_pointer -= 1
                
            ans_pointer -= 1
        
        if nums1_pointer >= 0:
            while ans_pointer >= 0:
                nums1[ans_pointer] = nums1[nums1_pointer]
                nums1_pointer -= 1
                ans_pointer -= 1
        
        if nums2_pointer >= 0:
            while ans_pointer >= 0:
                nums1[ans_pointer] = nums2[nums2_pointer]
                nums2_pointer -= 1
                ans_pointer -= 1