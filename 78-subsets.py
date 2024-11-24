from typing import List

test_case = [
    ([1, 2, 3], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]),
    ([0], [[], [0]]),
]


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for cur in nums:
            len_subsets = len(subsets)
            for i in range(len_subsets):
                subsets.append(subsets[i] + [cur])
        return subsets


for inp, out in test_case:
    try:
        actual = Solution().subsets(inp)
        assert actual == out
    except AssertionError:
        print(f"Inp: {inp}, expected {out}, got {actual}")
