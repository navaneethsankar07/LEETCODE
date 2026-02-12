class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        longest_duration = releaseTimes[0]
        slowest_key = keysPressed[0]
        for x in range(1,len(releaseTimes)):
            duration = releaseTimes[x] - releaseTimes[x-1]
            if duration > longest_duration:
                longest_duration = duration
                slowest_key = keysPressed[x]
            elif duration == longest_duration:
                slowest_key = max(slowest_key,keysPressed[x])
        return slowest_key