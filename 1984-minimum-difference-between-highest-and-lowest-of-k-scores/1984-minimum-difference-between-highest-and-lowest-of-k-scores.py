class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        best = float('inf')
        for right in range(len(nums)-k+1):
            best = min(best,(nums[right+k-1] - nums[right])) 
    
        return best 