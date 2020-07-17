"""
From July challenge

Logic:
Starting with the reverse, given x steps, how many coins, n, do you need?
n = (x^2 + x)  / 2

Do the reverse, you get a quadratic equation, solve it, take the positive val, floor the val
"""

import math


class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int(
            max((math.sqrt(1 + 8 * n) - 1) / 2, (-1 * math.sqrt(1 + 8 * n) - 1) / 2)
        )
