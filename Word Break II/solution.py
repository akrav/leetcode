class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        
        ans = []
        def rec(idx, path):
            if idx == n:
                ans.append(" ".join(path[:]))
                return
            
            for end in range(idx, n):
                if not in_dic(idx, end):
                    continue
                
                path.append(s[idx:end+1])
                rec(end+1, path)
                path.pop()
            
            return
            
        def in_dic(start, end):
            if s[start:end+1] in wordDict:
                return True
            return False
        
        rec(0, [])
        return ans