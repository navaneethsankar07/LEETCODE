class Solution:
    def averageValue(self, nums: List[int]) -> int:
        temp = [x for x in nums if x % 2 == 0 and x % 3 == 0]
        n = len(temp)
        return sum(temp)//n if n!= 0 else 0