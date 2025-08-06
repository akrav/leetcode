class Solution:
    def numDecodings(self, s: str) -> int:

        def rec(st):
            if st == '':
                return 1 

            
            first_letter = st[0]
            no_first_letter_count = 0
            if first_letter != '0' and int(first_letter) <= 26:
                no_first_letter = st[1:]
                no_first_letter_count = rec(no_first_letter)

            first_two_letters = st[:2]
            no_first_two_letters_count = 0
            if first_letter != '0' and len(first_two_letters) == 2 and int(first_two_letters) <= 26:
                no_first_two_letters = st[2:]
                no_first_two_letters_count = rec(no_first_two_letters)
            

            return no_first_letter_count + no_first_two_letters_count
        
        return rec(s)
        
# class Solution:
#     def numDecodings(self, s: str) -> int:

#         def rec(st):
#             # Base case: an empty string means we've found a valid decoding.
#             if st == '':
#                 return 1    

#             first_letter = st[0]
#             no_first_letter_count = 0
#             # If the first character is valid (non-'0'), decode it as a single digit.
#             if first_letter != '0':
#                 no_first_letter = st[1:]
#                 no_first_letter_count = rec(no_first_letter)
            
#             no_first_two_letters_count = 0
#             # If there are at least two characters and the two-digit number is valid,
#             # decode them as a pair.
#             if len(st) >= 2 and st[0] != '0' and int(st[:2]) <= 26:
#                 no_first_two_letters = st[2:]
#                 no_first_two_letters_count = rec(no_first_two_letters)
            
#             return no_first_letter_count + no_first_two_letters_count
        
#         return rec(s)