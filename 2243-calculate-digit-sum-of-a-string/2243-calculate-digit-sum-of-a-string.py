class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            temp = ""
            for x in range(0,len(s), k):
                temp += str(sum([int(i) for i in s[x: x + k]]))
            s = temp
        
        return s