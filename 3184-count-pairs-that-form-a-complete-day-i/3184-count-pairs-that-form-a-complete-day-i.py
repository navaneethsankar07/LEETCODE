class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        length = len(hours)
        count = 0
        for x in range(length-1):
            for y in range(x+1,length):
                if (hours[x] + hours[y]) % 24 == 0:
                    count +=1
        return count