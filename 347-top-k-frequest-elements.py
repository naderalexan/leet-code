from collections import defaultdict
from typing import List

test_case = [(([1, 1, 1, 2, 2, 3], 2), [1, 2]), (([3, 0, 1, 0], 1), [0])]


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for i in nums:
            freq[i] += 1
        res = list(dict(sorted(freq.items(), key=lambda x: x[1])).keys())[-k:]
        res.reverse()
        return res


for inp, out in test_case:
    try:
        actual = Solution().topKFrequent(*inp)
        assert actual == out
    except AssertionError:
        print(f"Inp: {inp}, expected {out}, got {actual}")
