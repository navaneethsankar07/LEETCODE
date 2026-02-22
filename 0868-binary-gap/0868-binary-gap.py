class Solution:
    def binaryGap(self, n: int) -> int:
        length =0
        binary = bin(n)[2:]
        left = binary.index('1')
        for x in range(len(binary)):
            if binary[x] == '1':
                length = max(length, x - left)
                left = x
        return length
