class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        temp = set(nums1)
        for x in nums2:
            if x in temp:
                return x
        
        return -1