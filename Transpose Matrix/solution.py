class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        tm = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
        # print(f"tm: {tm}")
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                tm[j][i] = matrix[i][j]
        
        return tm