[Back to Table of Contents](../README.md)

# N-Queens
Difficulty: Hard

## Question
N-Queens
Solved 
The n-queens puzzle is the problem of placing n queens on an n x n chessboard so that no two queens can attack each other.

A queen in a chessboard can attack horizontally, vertically, and diagonally.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a unique board layout where the queen pieces are placed. 'Q' indicates a queen and '.' indicates an empty space.

You may return the answer in any order.

Example 1:



Input: n = 4

Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There are two different solutions to the 4-queens puzzle.

Example 2:

Input: n = 1

Output: [["Q"]]
Constraints:

1 <= n <= 8

## Solution Template
```python
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1:
            return [["Q"]]
        board = [["." for _ in range(n)] for _ in range(n)]

        
        def is_valid(i, j):

            for col in range(j):
                if board[i][col]=="Q":
                    return False

            row = i
            col = j
            while row >= 0 and col >= 0:
                if board[row][col]=="Q":
                    return False
                row -= 1
                col -= 1

            row = i
            col = j
            while row < n and col >= 0:
                if board[row][col]=="Q":
                    return False
                row += 1
                col -= 1
            

            return True


        ans = []
        def rec(col):
            nonlocal ans
            if col == n:
                ans.append(["".join(row[:]) for row in board])
                return 


            for i in range(n):  
                if not is_valid(i, col):
                    continue
                board[i][col] = "Q"
                rec(col+1)
                board[i][col] = "."
            return 

        print(f"rec(0): {rec(0)}")
        print(f"ans: {ans}")
        return ans
            


        
        
```
