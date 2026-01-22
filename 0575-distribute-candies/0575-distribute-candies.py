class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        len_can = len(candyType)//2
        len_uni = len(set(candyType))
        if len_can == len_uni:
            return len_can
        elif len_can > len_uni:
            return len_uni
        else:
            return len_can