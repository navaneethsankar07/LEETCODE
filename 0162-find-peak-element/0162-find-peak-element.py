class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        peak_value = float('-inf')
        peak_index = 0
        for x in range(len(nums)):
            if nums[x] > peak_value:
                print(nums[x], peak_value)
                peak_value = nums[x]
                peak_index = x
        
        return peak_index