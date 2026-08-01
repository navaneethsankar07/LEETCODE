class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        answer = [0] * len(cost)
        current_min = float('inf')

        for x in range(len(cost)):
            current_min = min(current_min, cost[x])
            answer[x] = current_min
        
        return answer