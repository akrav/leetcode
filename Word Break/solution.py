class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        letter_to_word = defaultdict(list)
        memo = {}

        def rec(st):
            if st == '':
                return True
            
            if st in memo:
                return memo[st]
            
            overall = False
            for word in wordDict:
                if st[:len(word)] != word:
                    continue
                
                overall = overall or rec(st[len(word):])
            memo[st] = overall
            
            return overall
        
        return rec(s)

        