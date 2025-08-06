class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == word2:
            return 0
        
        n = len(word1)
        m = len(word2)
        memo = {}
        def rec(i, j):
            if i == n:
                return m - j
            
            if j == m:
                return n - i
            
            if (i,j) in memo:
                return memo[(i,j)]
            
            res = 10000000
            if word1[i] == word2[j]:
                res = rec(i + 1, j + 1)
            else:
                res = min(res, rec(i + 1, j), rec(i, j + 1), rec(i + 1, j + 1)) + 1
            
            memo[(i,j)] = res
            
            return res 
        
        return rec(0,0)