class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        mid = n // 2
        moves = 0
        for x in range(n):
            if x == mid:
                continue
            moves += abs(nums[mid] - nums[x])
        
        return moves

