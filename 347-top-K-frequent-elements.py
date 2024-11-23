from typing import List
from collections import Counter

test_cases = [
    (([1, 1, 1, 2, 2, 3], 2), [1, 2]),
    (([1], 1), [1]),
]


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sorted_occ = sorted(
            list(dict(Counter(nums)).items()), key=lambda x: x[1], reverse=True
        )
        res = []
        for i in range(k):
            res.append(sorted_occ[i][0])
        return res


for inp, out in test_cases:
    try:
        actual = Solution().topKFrequent(*inp)
        assert actual == out
    except AssertionError:
        print(f"Inp: {inp}, expected {out}, got {actual}")
