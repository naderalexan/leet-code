from typing import List

test_case = [
    ([1, 2, 2], [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]),
    ([0], [[], [0]]),
]


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = [[]]
        end = 0
        for index in range(len(nums)):
            start = 0
            if index > 0 and nums[index] == nums[index - 1]:
                start = end
            end = len(subsets)
            for i in range(start, end):
                subsets.append(subsets[i] + [nums[index]])
        return subsets


for inp, out in test_case:
    try:
        actual = Solution().subsetsWithDup(inp)
        assert actual == out
    except AssertionError:
        print(f"Inp: {inp}, expected {out}, got {actual}")
