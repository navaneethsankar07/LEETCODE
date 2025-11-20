class Solution:
    def isBalanced(self, num: str) -> bool:
        sum_odd = sum([int(num[x]) for x in range(1,len(num),2)])
        sum_even = sum([int(num[x]) for x in range(0,len(num),2)])
        return sum_odd == sum_even
             