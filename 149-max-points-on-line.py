from decimal import Decimal
from typing import List

test_case = [
    ([[1, 1], [2, 2], [3, 3]], 3),
    ([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]], 4),
    ([[1, 1], [2, 1], [3, 1]], 3),
    ([[1, 1], [1, 2], [1, 3]], 3),
    ([[1, 1], [1, 1], [1, 1]], 3),
    ([[0, 0], [94911150, 94911151], [94911151, 94911152]], 2),
    ([[0, 0], [94911151, 94911150], [94911152, 94911151]], 2),
]

from decimal import Decimal


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        VERTICAL = "vertical"
        l = len(points)
        if l < 3:
            return l
        result = 0
        for i in range(l):
            slopes = {}
            cur = points[i]
            same_points = 0
            for j in range(i + 1, l):
                nex = points[j]
                dx, dy = cur[0] - nex[0], cur[1] - nex[1]
                if dx == dy == 0:
                    same_points += 1
                elif dx == 0:
                    slopes[VERTICAL] = slopes.get(VERTICAL, 1) + 1
                else:
                    slope = Decimal(dy) / dx
                    slopes[slope] = slopes.get(slope, 1) + 1
            if slopes:
                cur_max = max(slopes.values()) + same_points
            else:
                cur_max = same_points + 1
            result = max(result, cur_max)
        return result


for inp, out in test_case:
    try:
        actual = Solution().maxPoints(inp)
        assert actual == out
    except AssertionError:
        print(f"Inp: {inp}, expected {out}, got {actual}")
