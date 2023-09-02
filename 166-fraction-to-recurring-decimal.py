test_case = [
    ((1, 2), "0.5"),
    ((2, 1), "2"),
    ((-2, 1), "-2"),
    ((2, 3), "0.(6)"),
    ((4, 333), "0.(012)"),
    ((1, 5), "0.2"),
    ((1, 6), "0.1(6)"),
]


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        sign = "-" if numerator * denominator < 0 else ""
        numerator, denominator = map(abs, (numerator, denominator))
        n, r = divmod(numerator, denominator)
        prefix = f"{sign}{n}"
        if not r:
            return prefix

        d = {}
        i = 0
        suffix = ""
        while r not in d:
            d[r] = i
            n, r = divmod(r * 10, denominator)
            suffix += str(n)
            if not r:
                return f"{prefix}.{suffix}"
            i += 1
        return f"{prefix}.{suffix[:d[r]]}({suffix[d[r]:]})"


for inp, out in test_case:
    try:
        actual = Solution().fractionToDecimal(*inp)
        assert actual == out
    except AssertionError:
        print(f"Inp: {inp}, expected {out}, got {actual}")
