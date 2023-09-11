import copy
from typing import List

test_case = [
    ([1, 1, 2], (2, [1, 2, 1])),
    ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], (5, [0, 1, 2, 3, 4, 0, 1, 1, 2, 3])),
    ([1, 1], (1, [1, 1])),
]


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        for i in range(len(nums)):
            if i < len(nums) - 1 and nums[i] == nums[i + 1]:
                continue
            nums[j], nums[i] = nums[i], nums[j]
            j += 1
        return j


for inp, out in test_case:
    try:
        inp_copy = copy.copy(inp)
        k_actual = Solution().removeDuplicates(inp)
        k, res = out
        assert k_actual == k
        assert res, inp
    except AssertionError:
        print(f"Inp: {inp_copy}, expected {out}, got ({k_actual}, {inp})")
