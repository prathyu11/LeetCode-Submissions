class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        countZero = nums.count(0)
        l = len(nums)
        if countZero > 1:
            return [0]*l

        op = [1]*l
        for i in range(l-1):
            op[i+1] = op[i]*nums[i]
        postfix=1
        for i in range(l-1, -1, -1):
            op[i] *= postfix
            postfix *= nums[i]

        return op
        


