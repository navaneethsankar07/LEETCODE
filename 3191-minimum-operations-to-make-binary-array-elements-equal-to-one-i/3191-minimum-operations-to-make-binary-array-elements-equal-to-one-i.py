class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        for x in range(len(nums)-2):
            if nums[x] == 1:
                continue
            
            nums[x] = 1
            nums[x+1] = 0 if nums[x+1] == 1 else 1
            nums[x+2] = 0 if nums[x+2] == 1 else 1
            count += 1
            print(nums)
        
        if 0 in nums:
            return -1
        
        return count

        
