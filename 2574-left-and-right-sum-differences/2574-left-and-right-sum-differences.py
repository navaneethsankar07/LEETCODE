class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left = []
        right = []
        for i in range(len(nums)):
            left.append(sum(nums[:i]))
            right.append(sum(nums[1+i:]))
        for i in range(len(nums)):
            nums[i] = abs(left[i] - right[i])
        return nums