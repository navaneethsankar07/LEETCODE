class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        indices = {}
        for i, num in enumerate(nums):
            if num not in indices:
                indices[num] = []
            indices[num].append(i)
        minimum = float('inf')

        for x in indices.values():
            if len(x) < 3:
                continue
            
            for i in range(len(x) - 2):
                distance = 2*(x[i+2] - x[i])
                minimum = min(distance, minimum)
        
        return minimum if minimum != float('inf') else -1
            

