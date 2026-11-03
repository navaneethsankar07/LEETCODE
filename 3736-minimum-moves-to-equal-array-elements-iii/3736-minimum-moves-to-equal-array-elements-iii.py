class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maxi = max(nums)
        moves = 0
        for x in nums:
            if x == maxi:
                continue
            moves += abs(maxi - x)
        
        return moves