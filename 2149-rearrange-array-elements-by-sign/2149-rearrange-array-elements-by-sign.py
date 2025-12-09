class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [0] * length
        pos = 0
        neg = 1
        for x in range(length):
            if nums[x] > 0:
                result[pos] = nums[x]
                pos += 2
            else:
                result[neg] = nums[x]
                neg += 2
        return result
