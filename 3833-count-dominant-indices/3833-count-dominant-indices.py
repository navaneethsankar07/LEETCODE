class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        count = 0
        total = sum(nums)
        n = len(nums)
        
        for i in range(n-1):
            total -= nums[i]
            right_count = n-i-1
            if nums[i] * right_count > total:
                count += 1
        
        return count