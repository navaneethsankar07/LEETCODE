class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        count = 0
        string_num = str(num)
        for i in range(len(string_num)-k+1):
            p = int(string_num[i:i+k])
            if p !=0 and  num % p == 0:
                count += 1
        return count 