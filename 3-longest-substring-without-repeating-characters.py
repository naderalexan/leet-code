test_case = [("abcabcbb", 3), ("bbbbb", 1), ("pwwkew", 3), (" ", 1), ("aabaab!bb", 3)]


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        cur = ""
        longest = 0
        for e in s:
            if e in cur:
                cur = cur[cur.index(e) + 1 :]
            cur += e
            longest = max(longest, len(cur))
        return longest


for inp, out in test_case:
    try:
        actual = Solution().lengthOfLongestSubstring(inp)
        assert actual == out
    except AssertionError:
        print(f"Inp: {inp}, expected {out}, got {actual}")
