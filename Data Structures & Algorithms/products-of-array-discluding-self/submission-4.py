class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]*len(nums)
        postfix = [1]*len(nums)
        op = [1]*len(nums)

        l=len(nums)
        pre=1
        post=1
        for i in range(l):
            prefix[i] = pre
            pre *= nums[i]
            
        for j in range(l-1,-1,-1):
            postfix[j] = post
            post *= nums[j]

        for k in range(l):
            op[k]=prefix[k]*postfix[k]

        return list(op)




