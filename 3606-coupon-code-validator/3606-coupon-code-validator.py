class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        valid = []
        bus = ["electronics", "grocery", "pharmacy", "restaurant"]
        for a,b,c in zip(isActive, businessLine, code):
            if a==True and b in bus and (c.isalnum()==True or '_' in c):
                valid.append((c,b))
        valid = sorted(valid, key = lambda item: (item[1],item[0]))
        return [x[0] for x in valid]