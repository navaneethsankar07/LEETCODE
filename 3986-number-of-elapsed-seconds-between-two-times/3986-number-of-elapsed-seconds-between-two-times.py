from datetime import datetime
class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        time1 = datetime.strptime(startTime, "%H:%M:%S")
        time2 = datetime.strptime(endTime, "%H:%M:%S")
        diff = (time1 - time2).total_seconds()
        return abs(int(diff))