class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        tested_devices = 0

        for x in batteryPercentages:
            if x - tested_devices > 0:
                tested_devices += 1
            
        return tested_devices