[Back to Table of Contents](../../README.md)

# Word Search
Difficulty: Medium

## Question
Word Search
Solved 
Given a 2-D grid of characters board and a string word, return true if the word is present in the grid, otherwise return false.

For the word to be present it must be possible to form it with a path in the board with horizontally or vertically neighboring cells. The same cell may not be used more than once in a word.

Example 1:



Input: 
board = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
],
word = "CAT"

Output: true
Example 2:



Input: 
board = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
],
word = "BAT"

Output: false
Constraints:

1 <= board.length, board[i].length <= 5
1 <= word.length <= 10
board and word consists of only lowercase and uppercase English letters.

## Solution Template
```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs_find(i, j, word):
            if word == "":
                return True
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
                return False
            if board[i][j] != word[0]:
                return False
            
            word1 = word[0]
            word = word[1:]
            hold = board[i][j]
            board[i][j] = "0"
            u = dfs_find(i + 1, j, word)
            d = dfs_find(i - 1, j, word)
            l = dfs_find(i, j + 1, word)
            r = dfs_find(i, j - 1, word)
            word = word1 + word
            board[i][j] = hold

            return u or d or l or r
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and dfs_find(i, j, word):
                    return True
        
        return False
            

        
```
