class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        for x in nums:
            if original in nums:
                print(original)
                original *=2
        return original