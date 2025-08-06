[Back to Table of Contents](../README.md)

# Decode Ways
Difficulty: Medium

## Question
Decode Ways
Solved 
A string consisting of uppercase english characters can be encoded to a number using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode a message, digits must be grouped and then mapped back into letters using the reverse of the mapping above. There may be multiple ways to decode a message. For example, "1012" can be mapped into:

"JAB" with the grouping (10 1 2)
"JL" with the grouping (10 12)
The grouping (1 01 2) is invalid because 01 cannot be mapped into a letter since it contains a leading zero.

Given a string s containing only digits, return the number of ways to decode it. You can assume that the answer fits in a 32-bit integer.

Example 1:

Input: s = "12"

Output: 2

Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: s = "01"

Output: 0
Explanation: "01" cannot be decoded because "01" cannot be mapped into a letter.

Constraints:

1 <= s.length <= 100
s consists of digits

## Solution Template
```python
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
```
