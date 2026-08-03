class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i,x in enumerate(nums):
            compl = target - x
            if compl in hmap:
                return [hmap[compl],i]
            hmap[x]=i
        return []

        

        