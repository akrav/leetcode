class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = defaultdict(int)
        left = 0
        right = 0
        max_length = 0

        while right < len(s):
            r_letter = s[right]

            count[r_letter] += 1

            # loop to check if we exceed used replacements
            # length of window minus most frequent character occurance
            # the remainder letters need to be replaced
            # if exceed move the left pointer and keep the count of the window

            while (right - left + 1) - max(count.values()) > k:
                l_letter = s[left]

                count[l_letter] -= 1
                left += 1
            
            # now a valid window, check if it is the largest size window
            max_length = max(max_length, (right - left) + 1)
            right += 1
        
        return max_length
