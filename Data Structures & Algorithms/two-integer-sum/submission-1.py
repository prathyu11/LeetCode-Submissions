class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idxmap = {}
        for i in range(len(nums)):
            complement = (target - nums[i])
            if complement in idxmap:
                return [idxmap[complement],i]
            idxmap[nums[i]] = i
        

        