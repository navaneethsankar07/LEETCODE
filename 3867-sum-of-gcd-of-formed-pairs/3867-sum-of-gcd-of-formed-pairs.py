import math
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefix_gcd = []
        current_max = 0

        for num in nums:
            current_max = max(current_max, num)
            prefix_gcd.append(math.gcd(num, current_max))

        prefix_gcd.sort()
        ans = 0 
        n = len(prefix_gcd)
        for x in range(n//2):
            ans += math.gcd(prefix_gcd[x],prefix_gcd[n-x-1])
        
        return ans