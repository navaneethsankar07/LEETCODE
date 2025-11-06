class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        original = [x for x in range(min(nums),max(nums)+1)]
        return [x for x in original if x not in nums]