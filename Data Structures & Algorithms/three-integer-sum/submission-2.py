class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sl = []
        for i in range(len(nums)-2):
            # skip duplicates
            if i>0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            j=i+1
            k=len(nums)-1
            
            while j<k:
                cp=nums[j]+nums[k]
                if cp==target:
                    sl.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    # skip duplicates
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1

                elif cp<target:
                    j+=1
                else:
                    k-=1
            
        return sl

