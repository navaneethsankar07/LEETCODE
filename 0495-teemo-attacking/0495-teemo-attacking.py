class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        time = 0
        for x in range(len(timeSeries)-1):
            diff = timeSeries[x+1] - timeSeries[x]
            time+=min(diff,duration)

        time += duration 

        return time