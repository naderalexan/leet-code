from collections import defaultdict

test_case = [
    ("AAAAAAAAAAA", ["AAAAAAAAAA"]),
    ("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT", ["AAAAACCCCC", "CCCCCAAAAA"]),
    ("AAAAAAAAAAAAA", ["AAAAAAAAAA"]),
]


class Solution:
    def findRepeatedDnaSequences(self, s: str):
        if len(s) <= 10:
            return []
        found = defaultdict(int)
        start = 0
        while start + 10 <= len(s):
            found[s[start : start + 10]] += 1
            start += 1

        result = []
        for key, val in found.items():
            if val > 1:
                result.append(key)
        return result


for inp, out in test_case:
    try:
        actual = Solution().findRepeatedDnaSequences(inp)
        assert actual == out
    except AssertionError:
        print(f"Inp: {inp}, expected {out}, got {actual}")
