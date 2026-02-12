class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        longest_duration = releaseTimes[0]
        slowest_key = keysPressed[0]
        for x in range(1,len(releaseTimes)):
            if releaseTimes[x] - releaseTimes[x-1] > longest_duration:
                longest_duration = releaseTimes[x] - releaseTimes[x-1]
                slowest_key = keysPressed[x]
            elif releaseTimes[x] - releaseTimes[x-1] == longest_duration:
                slowest_key = max(slowest_key,keysPressed[x])
        return slowest_key