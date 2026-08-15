class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(':')', '{':'}', "[":"]"}
        st = []
        for x in s:
            if x in d.keys():
                st.append(x)
            elif x in d.values():
                if not st or d[st.pop()]!=x:
                    return False
            else:
                return False
        return st == []
