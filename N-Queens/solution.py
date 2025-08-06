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
            


        
        