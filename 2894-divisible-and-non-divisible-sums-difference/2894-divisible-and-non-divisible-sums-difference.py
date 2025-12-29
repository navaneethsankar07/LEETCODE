class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        nums1 = [x for x in range(1,n+1) if x%m!=0]
        nums2 = [x for x in range(1,n+1) if x%m==0]
        return sum(nums1) - sum(nums2)