class Solution:
    def maximum69Number (self, num: int) -> int:
        new = str(num)
        for x in new:
            if x == '6':
                new = new.replace('6','9',1)
                break
        return int(new)