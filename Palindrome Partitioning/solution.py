class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.res = []

        def is_palindrome(word):
            l = 0
            r = len(word) - 1

            while l < r:
                if word[l] != word[r]:
                    return False
                l += 1
                r -= 1
            
            return True
        
        def dfs_combination_split(path, word):
            if word == "":
                self.res.append(path[:])
                return
            
            for i in range(1, len(word)+1):
                new_word = word[:i]

                if not is_palindrome(new_word):
                    continue
                
                path.append(new_word)
                dfs_combination_split(path, word[i:])
                path.pop()
        
        dfs_combination_split([], s)
        return self.res


        