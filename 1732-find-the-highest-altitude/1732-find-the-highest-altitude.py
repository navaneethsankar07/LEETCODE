class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        high = 0
        altitude = 0
        for x in gain:
            altitude += x
            if altitude > high:
                high = altitude
        
        return high