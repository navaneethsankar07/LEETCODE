class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        maxi = sum(tasks[0])
        for x in tasks:
            if sum(x) < maxi:
                maxi = sum(x)
        return maxi