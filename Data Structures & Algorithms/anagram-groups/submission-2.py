from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        tsmap = defaultdict(list)

        for s in strs:
            count = [0]*26
            for x in s:
                count[ord(x)-ord('a')] += 1
            tsmap[tuple(count)].append(s)
        
        return list(tsmap.values())





                

