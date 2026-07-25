class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        stack = []

        for x in range(n):
            if not stack or nums[stack[-1]] > nums[x]:
                stack.append(x)
        
        width = 0

        for y in range(n-1, -1, -1):
            while stack and nums[stack[-1]] <= nums[y]:
                width = max(width, y - stack.pop())
            
        return width        