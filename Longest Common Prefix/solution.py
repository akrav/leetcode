class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) <= 1:
            return '' if len(strs) == 0 else strs[0]
        
        prefix = strs[0]
        for i in range(1, len(strs)):
            new_prefix = ''
            for j in range(min(len(prefix), len(strs[i]))):
                if strs[i][j] != prefix[j]:
                    break
                new_prefix += strs[i][j]
            prefix = new_prefix
        
        return prefix