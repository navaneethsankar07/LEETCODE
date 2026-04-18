class Solution:
    def mirrorDistance(self, n: int) -> int:
        front = n
        rev = 0
        while front:
            digit = front % 10
            rev = rev * 10 + digit
            front = front//10
        return abs(n-rev)