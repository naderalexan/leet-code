test_cases = [(19, True), (2, False)]


class Solution:
    def get_nxt_val(self, n: int) -> int:
        output = 0
        while n:
            cur = n % 10
            n = n // 10
            output += cur ** 2
        return output

    def isHappy(self, n: int) -> bool:
        visited = set()
        while n not in visited:
            visited.add(n)
            n = self.get_nxt_val(n)
            if n == 1:
                return True
        return False


for inp, out in test_cases:
    try:
        actual = Solution().isHappy(inp)
        assert actual == out
    except AssertionError:
        print(f"Inp: {inp}, expected {out}, got {actual}")
