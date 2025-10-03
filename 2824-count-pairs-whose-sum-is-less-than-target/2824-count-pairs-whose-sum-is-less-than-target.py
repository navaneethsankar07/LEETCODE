class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        length = len(nums)
        pair = 0
        for x in range(length):
            for y in range(x+1,length):
                if nums[x] + nums[y] < target:
                    pair += 1
        return pair