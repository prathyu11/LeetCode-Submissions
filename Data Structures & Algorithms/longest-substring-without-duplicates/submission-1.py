class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sb = set()
        maxl =0
        l=0
        for r in range(len(s)):
            while s[r] in sb:
                sb.remove(s[l])
                l+=1
            sb.add(s[r])
            maxl = max(maxl,r-l+1)

        return maxl
            

