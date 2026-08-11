class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        prefix_sum = nums[0]
        for x in range(1,len(nums)):
            if nums[x] != nums[x-1] + 1:
                break
            else:
                prefix_sum += nums[x]
        
        nums.sort()

        for x in nums:
            if x == prefix_sum:
                prefix_sum += 1
            elif x > prefix_sum:
                break
        
        return prefix_sum