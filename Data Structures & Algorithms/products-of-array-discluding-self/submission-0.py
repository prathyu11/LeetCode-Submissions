class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        out = [0] * len(nums)
        res = 1
        zero_count = nums.count(0)
        if zero_count > 1:
            return out
            
        for x in nums:
            if x != 0:
                res *= x
        for i in range(len(nums)):
            if zero_count == 1:
                if nums[i] == 0:
                    out[i] = res
                else:
                    out[i] = 0
            else:
                out[i] = int(res/nums[i])

        return out