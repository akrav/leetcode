[Back to Table of Contents](../README.md)

# Longest Repeating Character Replacement
Difficulty: Medium

## Question
Longest Repeating Character Replacement
Solved 
You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.

After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

Example 1:

Input: s = "XYYX", k = 2

Output: 4
Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.

Example 2:

Input: s = "AAABABB", k = 1

Output: 5
Constraints:

1 <= s.length <= 1000
0 <= k <= s.length

## Solution Template
```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = defaultdict(int)
        left = 0
        right = 0
        max_length = 0

        while right < len(s):
            r_letter = s[right]

            count[r_letter] += 1

            # loop to check if we exceed used replacements
            # length of window minus most frequent character occurance
            # the remainder letters need to be replaced
            # if exceed move the left pointer and keep the count of the window

            while (right - left + 1) - max(count.values()) > k:
                l_letter = s[left]

                count[l_letter] -= 1
                left += 1
            
            # now a valid window, check if it is the largest size window
            max_length = max(max_length, (right - left) + 1)
            right += 1
        
        return max_length

```
