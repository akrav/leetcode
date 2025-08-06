# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
#         n = len(matrix)
#         m = len(matrix[0])

#         print(f"before: {matrix}")
#         for i in range(n):
#             for j in range(i, m):
#                 matrix[i][j], matrix[j][i]= matrix[j][i], matrix[i][j]
#         print(f"after: {matrix}")

#         for i in range(n):
#             left = 0
#             right = m - 1
#             while left < right:
#                 matrix[i][left], matrix[i][right]= matrix[i][right], matrix[i][left]
#                 left += 1
#                 right -= 1

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            for j in range(m):
                if i + j < n - 1:
                    matrix[i][j], matrix[n - 1 - j][n - 1 - i] = matrix[n - 1 - j][n - 1 - i], matrix[i][j]

        left = 0
        right = m - 1
        while left < right:
            matrix[left], matrix[right]= matrix[right], matrix[left]
            left += 1
            right -= 1

# before: [[1, 2, 3], 
#          [4, 5, 6], 
#          [7, 8, 9]]

# after: [[1, 4, 7], 
#         [2, 5, 8], 
#         [3, 6, 9]]

# after: [[9, 6, 3], 
#         [8, 5, 2], 
#         [7, 4, 1]]