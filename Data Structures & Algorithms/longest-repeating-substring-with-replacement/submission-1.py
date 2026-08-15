class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mf = 0
        ml = 0
        fm = {}
        l=0

        for r in range(len(s)):
            fm[s[r]] = fm.get(s[r],0)+1
            mf = max(mf,fm[s[r]])

            if (r-l+1) - mf > k:
                fm[s[l]] = fm.get(s[l],0)-1
                l += 1
            ml = max(ml,r-l+1)

        return ml
            

