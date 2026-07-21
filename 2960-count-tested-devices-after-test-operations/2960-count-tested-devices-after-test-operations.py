class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        tested_devices = 0
        n = len(batteryPercentages)
        for x in range(n):
            if batteryPercentages[x] <= 0: continue
            tested_devices += 1
            for j in range(x+1,n):
                batteryPercentages[j] -= 1
        
        return tested_devices
