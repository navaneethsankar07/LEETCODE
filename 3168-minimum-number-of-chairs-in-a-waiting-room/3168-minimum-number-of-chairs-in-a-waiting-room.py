class Solution:
    def minimumChairs(self, s: str) -> int:
        count = 0
        res = []
        for x in s:
            if x == 'E':
                count +=1
                res.append(count)
            else:
                count -=1
        return max(res)