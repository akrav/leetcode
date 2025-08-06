[Back to Table of Contents](../../README.md)

# Valid Palindrome
Difficulty: Easy

## Question
Valid Palindrome
Solved 
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

Example 2:

Input: s = "tab a cat"

Output: false
Explanation: "tabacat" is not a palindrome.

Constraints:

1 <= s.length <= 1000
s is made up of only printable ASCII characters.

## Solution Template
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) -1
        s = s.lower()

        while left < right:
            print(f"s[left]: {s[left]}, s[left].isalnum(): {s[left].isalnum()}")
            if s[left].isalnum() == False:
                left +=1
                continue
            print(f"s[right]: {s[right]}, s[right].isalnum(): {s[right].isalnum()}")
            if s[right].isalnum() == False:
                right -=1
                continue
            if s[left] != s[right]:
                return False
            left +=1
            right -=1
        
        return True
```
