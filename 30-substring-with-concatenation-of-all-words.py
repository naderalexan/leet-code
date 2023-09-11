from typing import List
from collections import Counter

test_case = [
    (("barfoothefoobarman", ["foo", "bar"]), [0, 9]),
    (("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]), []),
    (("barfoofoobarthefoobarman", ["bar", "foo", "the"]), [6, 9, 12]),
    (("wordgoodgoodgoodbestword", ["word", "good", "best", "good"]), [8]),
    (
        (
            "lingmindraboofooowingdingbarrwingmonkeypoundcake",
            ["fooo", "barr", "wing", "ding", "wing"],
        ),
        [13],
    ),
]


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words:
            return []
        res = []
        word_len = len(words[0])
        permutation_substring_len = word_len * len(words)
        for i in range(0, len(s) + 1):
            if i + permutation_substring_len <= len(s):
                cur = s[i : i + permutation_substring_len + 1]
                words_counter = Counter(words)
                for j in range(0, len(cur), word_len):
                    cur_word = cur[j : j + word_len]
                    if cur_word not in words_counter:
                        break
                    if words_counter[cur_word] > 1:
                        words_counter[cur_word] -= 1
                    else:
                        words_counter.pop(cur_word)
                if not words_counter:
                    res.append(i)
        return res


for inp, out in test_case:
    try:
        actual = Solution().findSubstring(*inp)
        assert actual == out
    except AssertionError:
        print(f"Inp: {inp}, expected {out}, got {actual}")
