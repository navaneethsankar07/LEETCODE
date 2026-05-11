class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        temp = ''.join(str(x) for x in nums)
        return list(int(x) for x in temp)