class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sb = []
        maxl =0
        for x in s:
            if x in sb:
                sb=sb[sb.index(x)+1:]
            sb.append(x)
            maxl = max(maxl,len(sb))
        return maxl
            

