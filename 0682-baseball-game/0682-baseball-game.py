class Solution:
    def calPoints(self, operations: List[str]) -> int:
        rec = []

        for x in operations:
            if x == 'D':
                rec.append(rec[-1]*2)
            elif x == '+':
                rec.append(rec[-1]+rec[-2])
            elif x == 'C':
                rec.pop()
            else:
                rec.append(int(x))
    
        return sum(rec)