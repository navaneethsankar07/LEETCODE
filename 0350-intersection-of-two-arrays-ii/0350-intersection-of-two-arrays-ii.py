class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq = {}
        res = []

        for x in nums1:
            freq[x] = freq.get(x,0) + 1
        

        for num in nums2:
            if num in freq and freq[num] > 0:
                res.append(num)
                freq[num] -= 1
        
        return res
