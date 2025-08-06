class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        alpha = defaultdict(lambda: -1)

        left = 0
        right = 0

        max_length = 0
        while right < len(s):
            letter = s[right]

            if alpha[letter] == -1:
                alpha[letter] = right
            else:
                left = max(left, alpha[letter] + 1)
                alpha[letter] = right
            print(f"left: {left}, right: {right}, (right - left): {(right - left)}, max_length: {max_length}")
            max_length = max(max_length, (right - left) + 1)
            print(f"left: {left}, right: {right}, (right - left): {(right - left)}, max_length: {max_length}")

            right += 1
        
        return max_length