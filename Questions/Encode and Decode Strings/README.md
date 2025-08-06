[Back to Table of Contents](../../README.md)

# Encode and Decode Strings
Difficulty: Medium

## Question
Encode and Decode Strings
Solved 
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]
Example 2:

Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]
Constraints:

0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.

## Solution Template
```python
class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for word in strs:
            ans += f"{len(word)}"+"#"+word
        print(f"encode: {ans}")
        return ans
    # "4#neet4#code4#love3#you"
    #  0123456789
    #  [2:6]

    def decode(self, s: str) -> List[str]:
        count = ""
        ans = []

        i = 0
        while i < len(s):
            print(f"s[i]: {s[i]}")
            if s[i] == "#":
                print(f"count: {count}")
                num_count = int(count)
                print(f"s[i+1: i+1+num_count]: {s[i+1: i+1+num_count]}")
                ans.append(s[i+1: i+1+num_count])
                i = i+num_count+1
                count = ""
            else:
                count += s[i]
                i += 1

        return ans
```
