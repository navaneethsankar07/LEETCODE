class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        final_sum = 0
        for val in nums:
            final_sum += int(str(max(str(val))*len(str(val))))
        return final_sum
