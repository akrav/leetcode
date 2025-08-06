class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        memo = {}
        def dfs(idx):
            if idx >= n:
                return 0
            if idx in memo:
                return memo[idx]
            
            curr_count = len(s)+1
            # option 1 is there a word in the dictionary take it and move fowards
            for word in dictionary:
                word_len = len(word)
                if s[idx:idx + word_len] == word:
                    curr_count =  min(curr_count, dfs(idx + word_len))

            
            # No word in the dictionary move idx plus 1
            curr_count = min(curr_count, dfs(idx + 1) + 1)

            memo[idx] = curr_count

            return curr_count
        
        
        
        return dfs(0)