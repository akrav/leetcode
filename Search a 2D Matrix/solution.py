class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #binary search row
        low = 0
        high = len(matrix) -1

        while low < high:
            mid = low + (high - low) // 2

            if target > matrix[mid][-1]:
                low = mid + 1
            elif target < matrix[mid][0]:
                high = mid - 1
            else:
                high = mid
        
        row = high

        # binary search col
        left = 0
        right = len(matrix[0]) - 1

        while left < right:
            mid = left + (right - left) // 2

            if target > matrix[row][mid]:
                left = mid + 1
            else:
                right = mid
        
        col = right

        return True if matrix[row][col] == target else False