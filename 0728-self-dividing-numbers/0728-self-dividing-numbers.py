class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for x in range(left,right+1):
            div = True
            con = str(x)
            if '0' in con:
                continue
            splited = list(map(int,str(x)))
            for y in splited:
                if x % y != 0:
                    div = False
                    break
            if div:
                result.append(x)
        return result
