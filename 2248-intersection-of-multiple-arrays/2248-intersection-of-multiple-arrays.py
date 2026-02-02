class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        intersection = []
        if len(nums) == 1:
            return sorted(nums[0])
        for x in range(1,len(nums)):
            if intersection:
                intersection = list(set(intersection) & set(nums[x]))
            else:
                intersection = list(set(nums[x-1]) & set(nums[x]))
        intersection.sort()
        return intersection