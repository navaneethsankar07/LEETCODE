from collections import defaultdict
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        window_length = 0
        left = 0
        freq = defaultdict(int)

        for right in range(len(nums)):
            freq[nums[right]] += 1

            while freq[nums[right]] > k:
                freq[nums[left]] -= 1
                left += 1
            

            window_length = max(window_length, right - left + 1)
        
        return window_length