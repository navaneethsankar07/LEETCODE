class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum, rightSum = 0, sum(nums)
        for i, x in enumerate(nums):
            rightSum -= x
            if leftSum == rightSum:
                return i
            leftSum += x
        
        return -1
