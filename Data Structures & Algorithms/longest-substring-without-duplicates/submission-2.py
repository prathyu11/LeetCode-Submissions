class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {} # dict of element:last idx of that element
        ml = 0
        l = 0

        for r in range(len(s)):
            if s[r] in last_seen and last_seen[s[r]]>=l:
                l = last_seen[s[r]]+1
            last_seen[s[r]] = r
            ml = max(ml, r-l+1)
        return ml

