[Back to Table of Contents](../../README.md)

# Surrounded Regions
Difficulty: Medium

## Question
Surrounded Regions
Solved 
You are given a 2-D matrix board containing 'X' and 'O' characters.

If a continous, four-directionally connected group of 'O's is surrounded by 'X's, it is considered to be surrounded.

Change all surrounded regions of 'O's to 'X's and do so in-place by modifying the input board.

Example 1:



Input: board = [
  ["X","X","X","X"],
  ["X","O","O","X"],
  ["X","O","O","X"],
  ["X","X","X","O"]
]

Output: [
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","X","X","O"]
]
Explanation: Note that regions that are on the border are not considered surrounded regions.

Constraints:

1 <= board.length, board[i].length <= 200
board[i][j] is 'X' or 'O'.

## Solution Template
```python
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        self.n = len(board)
        self.m = len(board[0])

        def dfs(i,j):
            if i < 0 or i >= self.n or \
               j < 0 or j >= self.m:
               return True
            
            b_val = board[i][j]

            if b_val == "X":
                return False

            if b_val == "Y":
                return True

            board[i][j] = "Y"
            u = dfs(i - 1,j)
            d = dfs(i + 1,j)
            l = dfs(i,j - 1)
            r = dfs(i,j + 1)


            return u and d and l and r

            
   
        

        for i in range(self.n):
            for j in range(self.m):
                if board[i][j] == "O" and (i == 0 or i == self.n-1 or j == self.m -1 or j == 0):
                    dfs(i,j)

        # Y means visited but not surrounded by X
        # need to convert back to O
        for i in range(self.n):
            for j in range(self.m):
                if board[i][j] == "O":
                    board[i][j] = "X"
        # Y means visited but not surrounded by X
        # need to convert back to O
        for i in range(self.n):
            for j in range(self.m):
                if board[i][j] == "Y":
                    board[i][j] = "O"
```
