[Back to Table of Contents](../README.md)

# Verifying An Alien Dictionary
Difficulty: Easy

## Question
Verifying an Alien Dictionary
Solved
Easy
Topics
premium lock icon
Companies
In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

 

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.

## Solution Template
```python
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        count = 1
        letter_order = {}
        for letter in order:
            letter_order[letter] = count
            count += 1
        

        for i in range(1, len(words)):
            word_1 = words[i-1]
            word_2 = words[i]
            same_beginning = True
            for j in range(min(len(word_1), len(word_2))):
                same_beginning = same_beginning and (word_1[j] == word_2[j])
                print(f"j: {j}, word_1[j]: {word_1[j]}, word_2[j]: {word_2[j]}")
                if letter_order[word_1[j]] < letter_order[word_2[j]]:
                    break
                elif letter_order[word_1[j]] > letter_order[word_2[j]]:
                    return False

            if same_beginning and len(word_1) > len(word_2):
                return False
                
        return True
        
```
