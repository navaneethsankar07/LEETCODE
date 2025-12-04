from collections import Counter
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        result = []
        real = [x for x in range(1,len(nums)+1)]
        for x in freq.items():
            if x[1] == 2:
                result.append(x[0])
            
        for x in real:
            if x not in nums:
                result.append(x)
        return result
                
