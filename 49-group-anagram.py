from collections import defaultdict
from typing import List

test_case = [
    (
        ["eat", "tea", "tan", "ate", "nat", "bat"],
        [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]],
    ),
]


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)
        for i in strs:
            dict["".join(sorted(i))].append(i)
        return list(dict.values())


for inp, out in test_case:
    try:
        actual = Solution().groupAnagrams(inp)
        assert actual == out
    except AssertionError:
        print(f"Inp: {inp}, expected {out}, got {actual}")
