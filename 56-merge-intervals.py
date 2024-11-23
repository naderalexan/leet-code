from typing import List

test_cases = [
    ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
    ([[1, 4], [4, 5]], [[1, 5]]),
    ([[1, 4], [0, 4]], [[0, 4]]),
]


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            last = res[-1]
            cur = intervals[i]
            if last[1] >= cur[0]:
                res[-1][1] = max(res[-1][1], cur[1])
            else:
                res.append(cur)
        return res


for inp, out in test_cases:
    try:
        actual = Solution().merge(inp)
        assert actual == out
    except AssertionError:
        print(f"Inp: {inp}, expected {out}, got {actual}")
