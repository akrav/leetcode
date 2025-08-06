class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for word in strs:
            ans += f"{len(word)}"+"#"+word
        print(f"encode: {ans}")
        return ans
    # "4#neet4#code4#love3#you"
    #  0123456789
    #  [2:6]

    def decode(self, s: str) -> List[str]:
        count = ""
        ans = []

        i = 0
        while i < len(s):
            print(f"s[i]: {s[i]}")
            if s[i] == "#":
                print(f"count: {count}")
                num_count = int(count)
                print(f"s[i+1: i+1+num_count]: {s[i+1: i+1+num_count]}")
                ans.append(s[i+1: i+1+num_count])
                i = i+num_count+1
                count = ""
            else:
                count += s[i]
                i += 1

        return ans