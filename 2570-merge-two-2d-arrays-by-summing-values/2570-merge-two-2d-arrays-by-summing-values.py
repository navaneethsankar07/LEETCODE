class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        left = 0
        res = []
        right = 0

        while left < len(nums1) and right < len(nums2):
            if nums1[left][0] == nums2[right][0]:
                res.append([nums1[left][0],nums1[left][1] + nums2[right][1]])
                left += 1
                right += 1
            elif nums1[left][0] < nums2[right][0]:
                res.append(nums1[left])
                left += 1
            else:
                res.append(nums2[right])
                right += 1
        
        if left < len(nums1):
            res.extend(nums1[left:])
        if right < len(nums2):
            res.extend(nums2[right:])
        
        return res