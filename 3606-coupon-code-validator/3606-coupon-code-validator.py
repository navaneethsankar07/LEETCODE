class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        allowed = {"electronics", "grocery", "pharmacy", "restaurant"}
        
        valid = []
        for c, b, a in zip(code, businessLine, isActive):
            if a and b in allowed and (c.isalnum() or "_" in c):
                valid.append((c, b))

        valid.sort(key=lambda x: (x[1], x[0]))
        
        return [c for c, _ in valid]
