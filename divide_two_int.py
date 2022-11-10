class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        is_pos = (dividend > 0) == (divisor >0)
        dividend =abs(dividend)
        divisor = abs(divisor)
        res = 0
        while dividend >= divisor:
            i =0
            while divisor<<(i+1) < dividend:
                i+=1
            res+= 1<< i
            dividend -= divisor<< i

        if res >= 1<<31 and is_pos:
            return (1<<31)-1
        if res >= 1<<31 and not is_pos:
            return -(1<<31)

        return res if is_pos else -res
