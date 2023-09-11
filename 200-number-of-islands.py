from typing import List

test_case = [
    (
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ],
        1,
    ),
    (
        [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ],
        3,
    ),
]


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            grid[i][j] = 0
            if i + 1 < len(grid) and int(grid[i + 1][j]):
                dfs(i + 1, j)
            if i - 1 >= 0 and int(grid[i - 1][j]):
                dfs(i - 1, j)
            if j + 1 < len(grid[i]) and int(grid[i][j + 1]):
                dfs(i, j + 1)
            if j - 1 >= 0 and int(grid[i][j - 1]):
                dfs(i, j - 1)

        res = 0
        for row in range(0, len(grid)):
            for col in range(0, len(grid[row])):
                if int(grid[row][col]):
                    res += 1
                    dfs(row, col)
        return res


for inp, out in test_case:
    try:
        actual = Solution().numIslands(inp)
        assert actual == out
    except AssertionError:
        print(f"Inp: {inp}, expected {out}, got {actual}")
