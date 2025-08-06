class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) -1
        s = s.lower()

        while left < right:
            print(f"s[left]: {s[left]}, s[left].isalnum(): {s[left].isalnum()}")
            if s[left].isalnum() == False:
                left +=1
                continue
            print(f"s[right]: {s[right]}, s[right].isalnum(): {s[right].isalnum()}")
            if s[right].isalnum() == False:
                right -=1
                continue
            if s[left] != s[right]:
                return False
            left +=1
            right -=1
        
        return True