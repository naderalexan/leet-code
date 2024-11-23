from typing import List

test_cases = [
    ([4, 3, 1, 4, 2], 4),
    ([1, 3, 4, 2, 2], 2),
    ([3, 1, 3, 4, 2], 3),
    ([3, 3, 3, 3, 3], 3),
]


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = f = nums[0]
        while 1:
            s = nums[s]
            f = nums[nums[f]]
            if s == f:
                break
        f = nums[0]
        while s != f:
            s = nums[s]
            f = nums[f]
        return s


for inp, out in test_cases:
    try:
        actual = Solution().findDuplicate(inp)
        assert actual == out
    except AssertionError:
        print(f"Inp: {inp}, expected {out}, got {actual}")
