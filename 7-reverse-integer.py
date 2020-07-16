class Solution:
    def reverse(self, x: int) -> int:
        mul = -1 if x < 0 else 1
        res = int(str(abs(x))[::-1]) * mul
        if -1 * pow(2, 31) < res < pow(2, 31) - 1:
            return res
        return 0
