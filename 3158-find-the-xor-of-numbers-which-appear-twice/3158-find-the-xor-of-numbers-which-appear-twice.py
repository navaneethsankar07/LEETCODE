from collections import Counter
class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        freq = Counter(nums)
        answers = [x for x,y in freq.items() if y == 2]
        xor = 0
        for x in answers:
            xor^=x
        return xor