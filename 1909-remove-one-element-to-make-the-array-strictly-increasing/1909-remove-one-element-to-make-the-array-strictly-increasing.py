class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        removed = False

        for x in range(1, len(nums)):
            if nums[x-1] >= nums[x]:
                if removed:
                    return False
                
                removed = True

                if x >= 2 and nums[x-2] >= nums[x]:
                    nums[x] = nums[x-1]
        
        return True