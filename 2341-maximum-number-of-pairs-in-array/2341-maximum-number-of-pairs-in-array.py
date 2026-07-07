from collections import Counter
class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        num_of_pairs = 0
        remaining = 0
        freq = Counter(nums)

        for x, y in freq.items():
            pairs = y//2
            print(pairs, y)
            num_of_pairs += pairs
            remaining += (y - 2* pairs)
        
        return [num_of_pairs, remaining]