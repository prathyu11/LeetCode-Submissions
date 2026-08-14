class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = {}
        mf = 0
        l = 0
        ml = 0

        for r in range(len(s)):
            hm[s[r]] = hm.get(s[r], 0) + 1
            mf = max(mf, hm[s[r]])

            while (r-l+1) - mf > k:
                hm[s[l]] -=1
                l+=1
            ml = max(ml,(r-l+1))

        return ml

