class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        index = float('inf')
        n = len(nums)
        for x in range(n):
            min_ = min(nums[x:n])
            max_ = max(nums[0:x+1])
            print(index, max_ - min_)
            if max_ - min_ <= k and x < index:

                index = x
        
        
        return index if index != float('inf') else -1 
