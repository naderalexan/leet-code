from typing import List

test_case = [
    (
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [1, 2, 4, 7, 5, 3, 6, 8, 9],
    ),
    (
        [[1, 2], [3, 4]],
        [1, 2, 3, 4],
    ),
    ([[1]], [1]),
    ([[3], [2]], [3, 2]),
]


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        def traverse(i, j, d):
            if i == len(mat) or j == len(mat[i]):
                return
            res.append(mat[i][j])

            # Continue in same direction
            if (
                d > 0
                and not (i == 0 or j == len(mat[i]) - 1)
                or d < 0
                and not (j == 0 or i == len(mat) - 1)
            ):
                traverse(i - d, j + d, d)
                return

            # Switch direction
            if d > 0:
                if j < len(mat[i]) - 1:
                    traverse(i, j + 1, -d)
                else:
                    traverse(i + 1, j, -d)
            else:
                if i < len(mat) - 1:
                    traverse(i + 1, j, -d)
                else:
                    traverse(i, j + 1, -d)

        if len(mat) == 0:
            return []

        res = []
        direction = 1
        traverse(0, 0, direction)
        return res


for inp, out in test_case:
    try:
        actual = Solution().findDiagonalOrder(inp)
        assert actual == out
    except AssertionError:
        print(f"Inp: {inp}, expected {out}, got {actual}")
