class Solution:
    def totalMoney(self, n: int) -> int:
        res = 0
        start = 0
        add = 0
        for x in range(n):
            if x % 7 == 0:
                start += 1
                res += start
                add = start + 1
            else:
                res += add 
                add += 1
            print(add)

        return res