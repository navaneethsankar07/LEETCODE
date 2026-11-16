class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            temp = []

            for x in range(0, len(s), k):
                chunk_sum = sum(int(i) for i in s[x:x+k])
                temp.append(str(chunk_sum))

            s = "".join(temp)

        return s