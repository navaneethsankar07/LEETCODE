class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        length = len(nums)
        for x in range(length):
            for y in range(x+1,length):
                if abs(nums[x] - nums[y]) == k:
                    count += 1
        return count