class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        moves = 0
        n = len(nums)
        mid = n // 2
        for x in range(n):
            if x == mid:
                continue
            
            moves += abs(nums[mid] - nums[x])

        return moves