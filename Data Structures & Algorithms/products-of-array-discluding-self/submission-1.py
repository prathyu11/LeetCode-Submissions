class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        out = [1] * len(nums)
        prefix = 1
        postfix = 1
        
        for i in range(1,len(nums)):
            out[i] = out[i-1] * nums[i-1]
        for i in range(len(nums)-1,-1,-1):
            out[i] *= postfix
            postfix *= nums[i]

        return out