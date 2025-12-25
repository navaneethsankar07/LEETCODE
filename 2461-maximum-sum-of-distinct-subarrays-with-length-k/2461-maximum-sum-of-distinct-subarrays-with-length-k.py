class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        left = 0
        max_sum = 0
        current = 0
        freq = {}
        for right in range(len(nums)):
            current += nums[right]
            freq[nums[right]] = freq.get(nums[right],0) + 1
            while freq[nums[right]] > 1 or right - left+1 > k:
                current -= nums[left]
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1

            if right - left + 1 == k:
                max_sum = max(max_sum,current)

        return max_sum
