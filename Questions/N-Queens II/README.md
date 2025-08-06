[Back to Table of Contents](../../README.md)

# N-Queens II
Difficulty: Hard

## Question
N-Queens II
Solved
Hard
Topics
premium lock icon
Companies
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

 

Example 1:


Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
Example 2:

Input: n = 1
Output: 1
 

Constraints:

1 <= n <= 9

## Solution Template
```python
class Solution:
    def totalNQueens(self, n: int) -> int:
        if n == 1:
            return 1

        board = [["." for _ in range(n)] for _ in range(n)]

        def is_valid(i, j):
            for col in range(j, -1, -1):
                if board[i][col] == "Q":
                    return False

            row = i
            col = j
            while row >= 0 and col >= 0:
                if board[row][col] == "Q":
                    return False
                row -= 1
                col -= 1
            
            row = i
            col = j
            while row < n and col >= 0:
                if board[row][col] == "Q":
                    return False
                row += 1
                col -= 1
            
            return True
        
        def rec(col):
            if col == n:
                print(f"board: {board}")
                return 1
            count = 0
            for i in range(n):
                if not is_valid(i, col):
                    continue
                
                board[i][col] = "Q"
                count += rec(col+1)
                board[i][col] = "."
            
            return count
        
        return rec(0)
```
