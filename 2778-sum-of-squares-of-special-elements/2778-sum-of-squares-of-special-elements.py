class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)

        for x in range(0, n):
            if n % (x+1) == 0:
                ans += (nums[x] * nums[x])
        
        return ans