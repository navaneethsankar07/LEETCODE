class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distinct = len(set(nums))
        count = 0
        n = len(nums)
        for x in range(n):
            seen = set()
            for y in range(x,n):
                seen.add(nums[y])
                if len(seen) == distinct:
                    count += n - y
                    break
        
        return count
            