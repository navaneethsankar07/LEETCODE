class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq = {}

        for x in arr1:
            freq[x] = freq.get(x,0) + 1
        
        result = []

        for num in arr2:
            if num in freq:
                result.extend([num]*freq[num])
                del freq[num]
        

        remaining = []

        for val, count in freq.items():
            remaining.extend([val]*count)
        
        result.extend(sorted(remaining))

        return result