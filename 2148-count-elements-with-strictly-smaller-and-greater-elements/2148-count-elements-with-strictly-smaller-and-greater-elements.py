class Solution:
    def countElements(self, nums: List[int]) -> int:
        count = 0
        mn = min(nums)
        mx = max(nums)

        for i in nums:
            if i > mn and i < mx:
                count += 1
            else:
                continue
        
        return count