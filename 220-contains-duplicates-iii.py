test_case = [
    (([1, 2, 3, 1], 3, 0), True),
    (([1, 0, 1, 1], 1, 2), True),
    (([1, 5, 9, 1, 5, 9], 2, 3), False),
    (([8, 7, 15, 1, 6, 1, 9, 15], 1, 3), True),
]


class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k: int, t: int) -> bool:
        if k < 0:
            return False

        buckets = {}
        width = t + 1
        for i, cur in enumerate(nums):
            key = cur // width
            if key in buckets:
                return True
            if key - 1 in buckets and abs(buckets[key - 1] - cur) < width:
                return True
            if key + 1 in buckets and abs(buckets[key + 1] - cur) < width:
                return True
            buckets[key] = cur
            if i >= k:
                del buckets[nums[i - k] // width]
        return False


for inp, out in test_case:
    try:
        actual = Solution().containsNearbyAlmostDuplicate(*inp)
        assert actual == out
    except AssertionError:
        print(f"Inp: {inp}, expected {out}, got {actual}")
