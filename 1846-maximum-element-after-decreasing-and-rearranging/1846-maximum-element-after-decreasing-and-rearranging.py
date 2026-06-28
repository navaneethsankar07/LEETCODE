class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        target = 1
        for x in arr:
            if x >= target:
                target += 1
        
        return target-1
