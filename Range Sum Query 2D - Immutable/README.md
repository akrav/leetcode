[Back to Table of Contents](../README.md)

# Range Sum Query 2D - Immutable
Difficulty: Medium

## Question
Range Sum Query 2D - Immutable
Solved
Medium
Topics
premium lock icon
Companies
Given a 2D matrix matrix, handle multiple queries of the following type:

Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
Implement the NumMatrix class:

NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
You must design an algorithm where sumRegion works on O(1) time complexity.

 

Example 1:


Input
["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
[[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
Output
[null, 8, 11, 12]

Explanation
NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
-104 <= matrix[i][j] <= 104
0 <= row1 <= row2 < m
0 <= col1 <= col2 < n
At most 104 calls will be made to sumRegion.

## Solution Template
```python
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix[:]
        self.matrix_sum = matrix[:]
        self.n = len(self.matrix)
        self.m = len(self.matrix[0])
        
        row_total = 0
        for i in range(self.n):
            row_total += self.matrix[i][0]
            self.matrix_sum[i][0] = row_total

        col_total = 0
        # print(f"self.m: {self.m}")
        for j in range(self.m):
            # print(f"j: {j}")
            col_total += self.matrix[0][j]
            self.matrix_sum[0][j] = col_total
        
        for i in range(1, self.n):
            for j in range(1, self.m):
                self.matrix_sum[i][j] = self.matrix_sum[i-1][j] + self.matrix_sum[i][j-1] + self.matrix[i][j] -  self.matrix_sum[i-1][j-1]
        


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        subtract_one = 0
        if row1 > 0:
            subtract_one = self.matrix_sum[row1-1][col2]

        subtract_two = 0
        if col1 > 0:
            subtract_two = self.matrix_sum[row2][col1-1]
        
        add_one = 0
        if row1 > 0 and col1 > 0:
            add_one = self.matrix_sum[row1 -1][col1-1]
        
        return self.matrix_sum[row2][col2] - subtract_one - subtract_two + add_one


        # Idea sum all squares from to top left to bottom right

        # Get sum in bottom right

        # Get square sum from row1 -1, col2 and row2, col1-1

        # add square of sum of row1 -1, col - 1
        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

[
    [3, 3, 4, 8, 10], 
    [8, 17, 24, 34, 45], 
    [9, 28, 52, 87, 137], 
    [13, 42, 94, 182, 326], 
    [14, 56, 153, 335, 666]]
```
