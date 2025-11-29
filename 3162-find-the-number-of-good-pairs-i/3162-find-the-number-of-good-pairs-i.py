class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        length1 = len(nums1)
        length2 = len(nums2)
        count = 0
        for x in range(length1):
            for y in range(length2):
                if nums1[x] % (nums2[y] * k ) == 0:
                    count += 1
        return count