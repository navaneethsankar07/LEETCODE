class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for x in range(len(nums)-1):
            if nums[x] == nums[x+1]:
                nums[x]*=2
                nums[x+1]=0
        j = 0
        for k in range(len(nums)):
            if nums[k]!=0:
                nums[k],nums[j]= nums[j],nums[k]
                j+=1
        return nums
            