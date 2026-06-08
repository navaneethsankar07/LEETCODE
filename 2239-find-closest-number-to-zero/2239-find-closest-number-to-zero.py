class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = float('inf')
        for x in nums:
            diff = abs(x)
            if diff < abs(closest):
                closest = x
            elif diff == abs(closest):
                closest = max(closest, x)
        
        return closest