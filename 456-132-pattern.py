from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        s = []
        last = None
        for cur in nums[::-1]:
            if last and last > cur:
                return True
            while s and s[-1] < cur:
                last = s.pop()
            s.append(cur)
        return False
