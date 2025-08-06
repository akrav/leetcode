class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def is_three_by_three_valid(n, m):
            row = n//3 * 3
            col = m//3 * 3
            check = defaultdict(bool)
            for i in range(row, row + 3):
                for j in range(col, col + 3):
                    if board[i][j] == '.':
                        continue
                    if check[board[i][j]]:
                        return False
                    check[board[i][j]] =True
            return True
        
        def is_row_valid(n, m):
            #n is row so we move across using m
            check = defaultdict(bool)
            for j in range(len(board[0])):
                if board[n][j] == '.':
                    continue
                if check[board[n][j]]:
                    return False
                check[board[n][j]] = True
            return True
        
        def is_col_valid(n, m):
            #n is row so we move across using m
            check = defaultdict(bool)
            for i in range(len(board)):
                if board[i][m] == '.':
                    continue
                if check[board[i][m]]:
                    return False
                check[board[i][m]] = True
            return True
        
        check = defaultdict(bool)
        for i in range(len(board)):
            for j in range(len(board[0])):
                box_check = True
                row_check = True
                col_check = True
                n = i//3
                m = j//3
                if check[f"{n},{m}"] == False:
                    box_check = is_three_by_three_valid(i, j)
                    check[f"{n},{m}"] = True
                row_check = is_row_valid(i, j)
                col_check = is_col_valid(i, j)

                if (box_check and row_check and col_check) == False:
                    return False
        return True
