class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for x in range(k):
            mini = nums.index(min(nums))
            minum = min(nums)
            nums[mini] = minum * multiplier

        return nums
            