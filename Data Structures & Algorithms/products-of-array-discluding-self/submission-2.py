class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        postfix = 1
        N = len(nums)
        output = [1]*N

        # prefix populated
        for i in range(N):
            output[i] = prefix
            prefix *= nums[i]

        # postfix is multiplied in place
        for j in range(N-1,-1,-1):
            output[j] *= postfix
            postfix *= nums[j]
        
        return output


