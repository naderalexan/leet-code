import math

test_case = [
    ([4, 2, 3], True),
    ([4, 2, 3, 2], False),
    ([1, 2, 0, 1], False),
]


class Solution:
    def checkPossibility(self, nums) -> bool:
        if len(nums) < 2:
            return True
        change_occurred = False
        prev = -math.inf
        for i, n in enumerate(nums):
            if prev > n:
                if change_occurred:
                    return False
                change_occurred = True
                if (
                    i - 2 >= 0
                    and nums[i - 2] > nums[i]
                    and i + 1 < len(nums)
                    and nums[i + 1] < nums[i - 1]
                ):
                    return False
            prev = n
        return True


for inp, out in test_case:
    try:
        actual = Solution().checkPossibility(inp)
        assert actual == out
    except AssertionError:
        print(f"Inp: {inp}, expected {out}, got {actual}")
