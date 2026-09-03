class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        _min = float('inf')
        odd_count = 0

        for x in nums1:
            _min = min(_min, x)
            if x % 2 == 1:
                odd_count += 1
        
        return _min % 2 == 1 or odd_count == 0