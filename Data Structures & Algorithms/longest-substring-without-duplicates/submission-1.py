class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # s = zxyzxyx
        left = 0
        seen = {}
        max_len = 0

        for right in range(len(s)):
            if s[right] in seen:
                left = max(left,seen[s[right]] + 1)
                

            seen[s[right]] = right
            max_len = max(max_len, right-left+1)
            
        # print(seen)
        return max_len

        