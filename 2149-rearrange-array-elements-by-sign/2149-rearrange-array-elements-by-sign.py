class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        pos = 0
        neg = 1
        for x in range(n):
            if nums[x] > 0:
                result[pos] = nums[x]
                pos += 2
            else:
                result[neg] = nums[x]
                neg += 2
        return result
