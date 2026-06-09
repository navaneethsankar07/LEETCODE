from datetime import datetime
class Solution:
    def dayOfYear(self, date: str) -> int:
        date = datetime.strptime(date, "%Y-%m-%d")
        return date.timetuple().tm_yday