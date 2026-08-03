class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ar = [0]*26
        if len(s)!=len(t):
            return False
        for i, x in enumerate(s):
            ar[ord(x)-ord('a')]= ar[ord(x)-ord('a')]+1
            ar[ord(t[i])-ord('a')]= ar[ord(t[i])-ord('a')]-1

        return not any(ar)