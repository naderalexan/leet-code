from typing import List

test_case = [
    ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]),
    ([0, 1], [[0, 1], [1, 0]]),
    ([1], [[1]]),
]


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start):
            if start == len(nums):
                res.append(nums[:])
                return
            for i in range(start, len(nums)):
                nums[i], nums[start] = nums[start], nums[i]
                backtrack(start + 1)
                nums[i], nums[start] = nums[start], nums[i]

        res = []
        backtrack(0)
        return res


for inp, out in test_case:
    try:
        actual = Solution().permute(inp)
        assert actual == out
    except AssertionError:
        print(f"Inp: {inp}, expected {out}, got {actual}")
