from typing import List

test_case = [
    ("a1b2", ["a1b2", "a1B2", "A1b2", "A1B2"]),
    ("3z4", ["3z4", "3Z4"]),
]


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def backtrack(s):
            if s == len(s_chars):
                res.append("".join(s_chars))
                return
            if s_chars[s].isalpha():
                s_chars[s] = s_chars[s].upper()
                backtrack(s + 1)

                s_chars[s] = s_chars[s].lower()
                backtrack(s + 1)
            else:
                backtrack(s + 1)

        s_chars = list(s)
        res = []
        backtrack(0)
        return res


for inp, out in test_case:
    try:
        actual = Solution().letterCasePermutation(inp)
        assert actual == out
    except AssertionError:
        print(f"Inp: {inp}, expected {out}, got {actual}")
