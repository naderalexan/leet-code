from collections import defaultdict
from typing import List

test_cases = [
    (
        ["alice,20,800,mtv", "alice,50,100,beijing"],
        ["alice,20,800,mtv", "alice,50,100,beijing"],
    ),
    (["alice,20,800,mtv", "alice,50,1200,mtv"], ["alice,50,1200,mtv"]),
    (["alice,20,800,mtv", "bob,50,1200,mtv"], ["bob,50,1200,mtv"]),
]


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        conflict_checker = defaultdict(list)
        conflict_indecies = set()
        for i, t in enumerate(transactions):
            [name, time, amount, city] = t.split(",")
            time = int(time)
            amount = int(amount)
            conflict_checker[name].append((i, time, city))
            for it_i, it_time, it_city in conflict_checker[name]:
                if abs(it_time - time) <= 60 and city != it_city:
                    conflict_indecies.add(i)
                    conflict_indecies.add(it_i)
                elif amount > 1000:
                    conflict_indecies.add(i)

        return [transactions[i] for i in conflict_indecies]


for inp, out in test_cases:
    try:
        actual = Solution().invalidTransactions(inp)
        assert actual == out
    except AssertionError:
        print(f"Inp: {inp}, expected {out}, got {actual}")
