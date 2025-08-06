[Back to Table of Contents](../../README.md)

# Letter Combinations of a Phone Number
Difficulty: Medium

## Question
Letter Combinations of a Phone Number
Solved 
You are given a string digits made up of digits from 2 through 9 inclusive.

Each digit (not including 1) is mapped to a set of characters as shown below:

A digit could represent any one of the characters it maps to.

Return all possible letter combinations that digits could represent. You may return the answer in any order.



Example 1:

Input: digits = "34"

Output: ["dg","dh","di","eg","eh","ei","fg","fh","fi"]
Example 2:

Input: digits = ""

Output: []
Constraints:

0 <= digits.length <= 4
2 <= digits[i] <= 9

## Solution Template
```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
            
        dic = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        self.res = []

        def dfs(digits_string, path):
            if digits_string == "":
                self.res.append(path)
                return

            digit = digits_string[0]
            letter_set = dic[digit]
            for i in range(len(letter_set)):
                path += letter_set[i]
                dfs(digits_string[1:], path)
                path = path[:-1]
        
        dfs(digits, "")
        return self.res
```
