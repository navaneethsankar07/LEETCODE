class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        count = 0
        for x in range(len(hours)-1):
            for y in range(x+1,len(hours)):
                if (hours[x] + hours[y]) % 24 == 0:
                    count +=1
        return count