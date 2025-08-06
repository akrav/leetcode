class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs_find(i, j, word):
            if word == "":
                return True
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
                return False
            if board[i][j] != word[0]:
                return False
            
            word1 = word[0]
            word = word[1:]
            hold = board[i][j]
            board[i][j] = "0"
            u = dfs_find(i + 1, j, word)
            d = dfs_find(i - 1, j, word)
            l = dfs_find(i, j + 1, word)
            r = dfs_find(i, j - 1, word)
            word = word1 + word
            board[i][j] = hold

            return u or d or l or r
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and dfs_find(i, j, word):
                    return True
        
        return False
            

        