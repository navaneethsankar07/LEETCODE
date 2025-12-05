class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        for x in range(n-1):
            left = sum(nums[0:x+1])
            right = sum(nums[x+1:n])
            if abs(left-right)%2 == 0:
                count += 1
        return count