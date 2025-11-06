class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        maxi = max(nums)
        sum = 0    
        for x in range(k):
            sum += maxi
            maxi+=1
        return sum