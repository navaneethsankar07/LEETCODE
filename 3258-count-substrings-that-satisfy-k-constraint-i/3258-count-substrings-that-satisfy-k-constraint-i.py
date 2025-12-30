class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        left,res,one = 0,0,0
        for right, num in enumerate(s):
            one += 1 if num == '1' else 0
            while one > k and right-left+1-one > k:
               one -= 1  if s[left] == '1' else 0
               left += 1

            res += right - left + 1

        return res