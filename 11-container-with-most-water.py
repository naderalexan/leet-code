from typing import List

test_cases = [
    ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
    ([1, 1], 1),
    ([1, 3, 2, 5, 25, 24, 5], 24),
]


class Solution:
    def area(self, start, end, height):
        shorter = min(height[start], height[end])
        return shorter * (end - start)

    def maxArea(self, height: List[int]) -> int:
        start, end = 0, len(height) - 1
        water = 0
        while start < end:
            area = self.area(start, end, height)
            water = max(water, area)
            if height[end] > height[start]:
                start += 1
            else:
                end -= 1
        return water


for inp, out in test_cases:
    try:
        actual = Solution().maxArea(inp)
        assert actual == out
    except AssertionError:
        print(f"Inp: {inp}, expected {out}, got {actual}")
