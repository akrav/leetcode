class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])

        left = 0
        right = m
        bottom = 0
        up = n

        ans = []
        while left < right and bottom < up:
            for i in range(left, right):
                ans.append(matrix[bottom][i])
            bottom += 1

            for i in range(bottom, up):
                ans.append(matrix[i][right-1])
            right -= 1

            if left >= right or bottom >= up:
                break
                
            for i in range(right-1, left-1, -1):
                ans.append(matrix[up-1][i])
            up -= 1


            for i in range(up -1, bottom -1, -1):
                ans.append(matrix[i][left])
            left += 1

        return ans