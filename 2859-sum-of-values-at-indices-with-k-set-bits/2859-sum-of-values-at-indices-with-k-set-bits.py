class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        total = 0

        for x in range(len(nums)):
            if bin(x).count('1') == k:
                total += nums[x]
        
        return total