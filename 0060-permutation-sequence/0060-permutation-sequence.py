from itertools import permutations
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        num = [x for x in range(1,n+1)]
        perm_list = list(permutations(num))
        return ''.join(map(str,perm_list[k-1]))
