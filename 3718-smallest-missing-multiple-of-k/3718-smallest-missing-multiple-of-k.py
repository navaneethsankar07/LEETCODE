class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        s = set(nums)
        x = 1
        while True:
            if k * x not in s:
                return k * x
            x+=1