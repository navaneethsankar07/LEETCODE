class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        win_sum = sum(nums[:k])
        best = win_sum

        for i in range(k,len(nums)):
            win_sum += nums[i]
            win_sum -= nums[i-k]
            best = max(best,win_sum)
        
        return best/k