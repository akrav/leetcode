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