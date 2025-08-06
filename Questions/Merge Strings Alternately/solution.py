class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)

        i = 0
        j = 0
        
        ans = ""
        while i < n and j < m:
            ans += word1[i] + word2[j]
            i += 1
            j+= 1
        
        if i < n:
            ans += word1[i:]
        
        if j < m:
            ans += word2[j:]
        
        return ans

        