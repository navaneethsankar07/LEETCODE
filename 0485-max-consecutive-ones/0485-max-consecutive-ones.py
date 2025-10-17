class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maximum = 0
        for x in nums:
            if x == 1:
                count += 1
                maximum = max(maximum,count)
            if x == 0: 
                    count = 0

        return maximum