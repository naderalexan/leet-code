from typing import List

test_cases = [
    ([7, [2, 3, 1, 2, 4, 3]], 2),
    ([7, []], 0),
    ([4, [1, 4, 4]], 1),
]


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        l = len(nums)
        ans = float("Inf")
        mysum = 0
        left = 0
        for right in range(l):
            mysum += nums[right]
            while mysum >= s and left <= right:
                ans = min(ans, right - left + 1)
                mysum -= nums[left]
                left += 1
        return ans if ans < float("Inf") else 0


for inp, out in test_cases:
    try:
        actual = Solution().minSubArrayLen(*inp)
        assert actual == out
    except AssertionError:
        print(f"Inp: {inp}, expected {out}, got {actual}")
