class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        op = [1]*len(nums)
        l=len(nums)
        pre=1
        post=1
        for i in range(l):
            op[i] = pre
            pre *= nums[i]
            
        for j in range(l-1,-1,-1):
            op[j] *= post
            post *= nums[j]

        return op




