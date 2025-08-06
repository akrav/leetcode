class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1 = len(str1)
        len2 = len(str2)

        def is_Divisor(str_len):
            if len1 % str_len != 0 or len2 % str_len != 0:
                return False
            str1_num_of_repeats = len1//str_len
            str2_num_of_repeats = len2//str_len
            return ((str1[:str_len] * str1_num_of_repeats) == str1) and ((str1[:str_len] * str2_num_of_repeats) == str2)
        
        for i in range(min(len1, len2), 0, -1):
            if is_Divisor(i):
                return str1[:i]
        
        return ""