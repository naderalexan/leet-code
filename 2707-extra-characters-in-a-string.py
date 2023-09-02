from typing import List

test_cases = [
    (
        [
            "dwmodizxvvbosxxw",
            [
                "ox",
                "lb",
                "diz",
                "gu",
                "v",
                "ksv",
                "o",
                "nuq",
                "r",
                "txhe",
                "e",
                "wmo",
                "cehy",
                "tskz",
                "ds",
                "kzbu",
            ],
        ],
        7,
    ),
    (
        [
            "azvzulhlwxwobowijiyebeaskecvtjqwkmaqnvnaomaqnvf",
            [
                "na",
                "i",
                "edd",
                "wobow",
                "kecv",
                "b",
                "n",
                "or",
                "jj",
                "zul",
                "vk",
                "yeb",
                "qnfac",
                "azv",
                "grtjba",
                "yswmjn",
                "xowio",
                "u",
                "xi",
                "pcmatm",
                "maqnv",
            ],
        ],
        15,
    ),
]


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dic_set = set(dictionary)
        dp = {len(s): 0}

        def dfs(i):
            if i in dp:
                return dp[i]

            res = 1 + dfs(i + 1)
            for j in range(i, len(s)):
                if s[i : j + 1] in dic_set:
                    res = min(res, dfs(j + 1))
            dp[i] = res
            return res

        return dfs(0)


for inp, out in test_cases:
    try:
        actual = Solution().minExtraChar(*inp)
        assert actual == out
    except AssertionError:
        print(f"Inp: {inp}, expected {out}, got {actual}")
