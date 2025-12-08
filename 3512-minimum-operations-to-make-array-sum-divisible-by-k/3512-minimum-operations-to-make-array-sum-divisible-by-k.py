class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0
        total = sum(nums)
        while total % k != 0:
            count += 1
            total -= 1

        return count
            

