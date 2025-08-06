class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)
        o = len(s3)

        if n + m != o:
            return False
        
        def rec(i, j, path):
            if path != s3[:len(path)]:
                return False
            if i >= n and j >= m:
                if path == s3:
                    return True
                return False

            res = False
            if i < n :
                s3_idx = i + j

                path = path + s1[i]
                res = res or rec(i + 1, j, path)
                path = path[:-1]

            if j < m:
                path = path + s2[j]
                res = res or rec(i, j + 1, path)
                path = path[:-1]

            
            return res

        return rec(0, 0, '')
            
            