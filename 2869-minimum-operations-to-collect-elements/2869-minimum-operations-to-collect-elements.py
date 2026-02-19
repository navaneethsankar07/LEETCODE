class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        needed = set(range(1,k+1))
        operations = 0
        for x in reversed(nums):
            operations += 1
            needed.discard(x)

            if not needed:
                return operations